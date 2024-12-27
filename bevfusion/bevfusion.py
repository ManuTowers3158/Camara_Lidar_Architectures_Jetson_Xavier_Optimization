from collections import OrderedDict
from copy import deepcopy
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.distributed as dist
from mmengine.utils import is_list_of
from torch import Tensor
from torch.nn import functional as F
import time
from datetime import datetime
import spconv
from mmdet3d.models import Base3DDetector
from mmdet3d.registry import MODELS
from mmdet3d.structures import Det3DDataSample
from mmdet3d.utils import OptConfigType, OptMultiConfig, OptSampleList
from .ops import Voxelization
from torch.cuda.amp import autocast
import matplotlib.pyplot as plt

@MODELS.register_module()
class BEVFusion(Base3DDetector):

    def __init__(
            self,
            data_preprocessor: OptConfigType = None,
            pts_voxel_encoder: Optional[dict] = None,
            pts_middle_encoder: Optional[dict] = None,
            fusion_layer: Optional[dict] = None,
            img_backbone: Optional[dict] = None,
            pts_backbone: Optional[dict] = None,
            view_transform: Optional[dict] = None,
            img_neck: Optional[dict] = None,
            pts_neck: Optional[dict] = None,
            bbox_head: Optional[dict] = None,
            init_cfg: OptMultiConfig = None,
            seg_head: Optional[dict] = None,
            **kwargs,
    ) -> None:
        voxelize_cfg = data_preprocessor.pop('voxelize_cfg')
        super().__init__(
            data_preprocessor=data_preprocessor, init_cfg=init_cfg)

        self.voxelize_reduce = voxelize_cfg.pop('voxelize_reduce')
        self.pts_voxel_layer = Voxelization(**voxelize_cfg)

        self.pts_voxel_encoder = MODELS.build(pts_voxel_encoder)

        self.img_backbone = MODELS.build(
            img_backbone) if img_backbone is not None else None
        self.img_neck = MODELS.build(
            img_neck) if img_neck is not None else None
        self.view_transform = MODELS.build(
            view_transform) if view_transform is not None else None
        self.pts_middle_encoder = MODELS.build(pts_middle_encoder)

        self.fusion_layer = MODELS.build(
            fusion_layer) if fusion_layer is not None else None

        self.pts_backbone = MODELS.build(pts_backbone)
        self.pts_neck = MODELS.build(pts_neck)

        self.bbox_head = MODELS.build(bbox_head)

        self.init_weights()

    def _forward(self,
                 batch_inputs: Tensor,
                 batch_data_samples: OptSampleList = None):
        """Network forward process.

        Usually includes backbone, neck and head forward without any post-
        processing.
        """
        pass

    def parse_losses(
            self, losses: Dict[str, torch.Tensor]
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        """Parses the raw outputs (losses) of the network.

        Args:
            losses (dict): Raw output of the network, which usually contain
                losses and other necessary information.

        Returns:
            tuple[Tensor, dict]: There are two elements. The first is the
            loss tensor passed to optim_wrapper which may be a weighted sum
            of all losses, and the second is log_vars which will be sent to
            the logger.
        """
        log_vars = []
        for loss_name, loss_value in losses.items():
            if isinstance(loss_value, torch.Tensor):
                log_vars.append([loss_name, loss_value.mean()])
            elif is_list_of(loss_value, torch.Tensor):
                log_vars.append(
                    [loss_name,
                     sum(_loss.mean() for _loss in loss_value)])
            else:
                raise TypeError(
                    f'{loss_name} is not a tensor or list of tensors')

        loss = sum(value for key, value in log_vars if 'loss' in key)
        log_vars.insert(0, ['loss', loss])
        log_vars = OrderedDict(log_vars)  # type: ignore

        for loss_name, loss_value in log_vars.items():
            # reduce loss when distributed training
            if dist.is_available() and dist.is_initialized():
                loss_value = loss_value.data.clone()
                dist.all_reduce(loss_value.div_(dist.get_world_size()))
            log_vars[loss_name] = loss_value.item()

        return loss, log_vars  # type: ignore

    def init_weights(self) -> None:
        if self.img_backbone is not None:
            self.img_backbone.init_weights()

    @property
    def with_bbox_head(self):
        """bool: Whether the detector has a box head."""
        return hasattr(self, 'bbox_head') and self.bbox_head is not None

    @property
    def with_seg_head(self):
        """bool: Whether the detector has a segmentation head.
        """
        return hasattr(self, 'seg_head') and self.seg_head is not None

    def extract_img_feat(
            self,
            x,
            points,
            lidar2image,
            camera_intrinsics,
            camera2lidar,
            img_aug_matrix,
            lidar_aug_matrix,
            img_metas,
    ) -> torch.Tensor:
        B, N, C, H, W = x.size()
        x = x.view(B * N, C, H, W).contiguous()

        # Capture initial GPU memory usage for camera backbone
        #initial_mem_backbone = torch.cuda.memory_allocated()

        # Camera backbone processing
        x = self.img_backbone(x)

        # Capture final GPU memory usage for camera backbone
        #final_mem_backbone = torch.cuda.memory_allocated()

        # Print memory used by camera backbone
        #print(f"Memory used by camera backbone: {final_mem_backbone - initial_mem_backbone} bytes")

        # Capture initial GPU memory usage for camera neck
        # initial_mem_neck = torch.cuda.memory_allocated()

        # **Camera neck processing**
        x = self.img_neck(x)

        # Capture final GPU memory usage for camera neck
        #final_mem_neck = torch.cuda.memory_allocated()

        # Print memory used by camera neck
        #print(f"Memory used by camera neck: {final_mem_neck - initial_mem_neck} bytes")
        # If img_neck returns a tuple, take the first element


        if not isinstance(x, torch.Tensor):
            x = x[0]

        BN, C, H, W = x.size()
        x = x.view(B, int(BN / B), C, H, W)

        # View transformation processing
        with torch.autocast(device_type='cuda', dtype=torch.float32):
            x = self.view_transform(
                x,
                points,
                lidar2image,
                camera_intrinsics,
                camera2lidar,
                img_aug_matrix,
                lidar_aug_matrix,
                img_metas,
            )

        return x

    # # *********extract image original*****
    # def extract_img_feat(
    #         self,
    #         x,
    #         points,
    #         lidar2image,
    #         camera_intrinsics,
    #         camera2lidar,
    #         img_aug_matrix,
    #         lidar_aug_matrix,
    #         img_metas,
    # ) -> torch.Tensor:
    #     B, N, C, H, W = x.size()
    #     x = x.view(B * N, C, H, W).contiguous()
    #
    #     # Synchronize before starting the camera backbone timing
    #     torch.cuda.synchronize()
    #     camera_backbone_start_time = time.time()
    #
    #     # Camera backbone processing
    #     x = self.img_backbone(x)
    #
    #     # Synchronize after camera backbone processing
    #     torch.cuda.synchronize()
    #     camera_backbone_end_time = time.time()
    #     camera_backbone_elapsed = camera_backbone_end_time - camera_backbone_start_time
    #     print(f"Time taken by the camera backbone: {camera_backbone_elapsed:.4f} seconds")
    #
    #     # Synchronize before starting the camera neck timing
    #     torch.cuda.synchronize()
    #     camera_neck_start_time = time.time()
    #
    #     # **Camera neck processing**
    #     x = self.img_neck(x)
    #
    #     # Synchronize after camera neck processing
    #     torch.cuda.synchronize()
    #     camera_neck_end_time = time.time()
    #     camera_neck_elapsed = camera_neck_end_time - camera_neck_start_time
    #     print(f"Time taken by the camera neck: {camera_neck_elapsed:.4f} seconds")
    #
    #     if not isinstance(x, torch.Tensor):
    #         x = x[0]
    #
    #     BN, C, H, W = x.size()
    #     x = x.view(B, int(BN / B), C, H, W)
    #     # Log time for view transformation
    #     torch.cuda.synchronize()  # Synchronize before starting the timer
    #     view_transform_start_time = time.time()
    #
    #     with torch.autocast(device_type='cuda', dtype=torch.float32):
    #         x = self.view_transform(
    #             x,
    #             points,
    #             lidar2image,
    #             camera_intrinsics,
    #             camera2lidar,
    #             img_aug_matrix,
    #             lidar_aug_matrix,
    #             img_metas,
    #         )
    #     torch.cuda.synchronize()  # Synchronize after view transformation
    #     view_transform_end_time = time.time()
    #     view_transform_elapsed_time = view_transform_end_time - view_transform_start_time
    #     print(f"Time taken for view transformation: {view_transform_elapsed_time:.4f} seconds")
    #
    #     return x

    # def extract_pts_feat(self, batch_inputs_dict) -> torch.Tensor: #******ORIGINAL*****
    #     points = batch_inputs_dict['points']
    #
    #     # Synchronize before starting timing
    #     torch.cuda.synchronize()
    #     start_time = time.time()
    #
    #     with torch.autocast('cuda', enabled=False):
    #         points = [point.float() for point in points]
    #         feats, coords, sizes = self.voxelize(points)
    #         batch_size = coords[-1, 0] + 1
    #
    #     x = self.pts_middle_encoder(feats, coords, batch_size)
    #
    #     # Synchronize after finishing timing
    #     torch.cuda.synchronize()
    #     end_time = time.time()
    #
    #     # Compute elapsed time
    #     elapsed_time = end_time - start_time
    #     print(f"Time taken by the lidar processing stage: {elapsed_time:.4f} seconds")
    #
    #     return x

    def extract_pts_feat(self, batch_inputs_dict) -> torch.Tensor:
        points = batch_inputs_dict['points']

        # Synchronize before starting timing
        torch.cuda.synchronize()
        start_time = time.time()

        with torch.autocast('cuda', enabled=False):
            points = [point.float() for point in points]
            feats, coords, sizes = self.voxelize(points)
            batch_size = coords[-1, 0] + 1
        # Synchronize after finishing timing
        torch.cuda.synchronize()
        end_time = time.time()
        # Compute elapsed time
        elapsed_time = end_time - start_time
        #print(f"Time taken by the lidar voxelization: {elapsed_time:.4f} seconds")

        # Synchronize before starting timing
        torch.cuda.synchronize()
        start_time = time.time()
        x = self.pts_middle_encoder(feats, coords, batch_size)
        # Synchronize after finishing timing
        torch.cuda.synchronize()
        end_time = time.time()

        # Compute elapsed time
        elapsed_time = end_time - start_time
        #print(f"Time taken by the lidar middle encoder: {elapsed_time:.4f} seconds")

        return x

    @torch.no_grad()  # ********ORIGINAL
    def voxelize(self, points):
        feats, coords, sizes = [], [], []
        for k, res in enumerate(points):
            ret = self.pts_voxel_layer(res)
            if len(ret) == 3:
                # hard voxelize
                f, c, n = ret
            else:
                assert len(ret) == 2
                f, c = ret
                n = None
            feats.append(f)
            coords.append(F.pad(c, (1, 0), mode='constant', value=k))
            if n is not None:
                sizes.append(n)

        feats = torch.cat(feats, dim=0)
        coords = torch.cat(coords, dim=0)
        if len(sizes) > 0:
            sizes = torch.cat(sizes, dim=0)
            if self.voxelize_reduce:
                feats = feats.sum(
                    dim=1, keepdim=False) / sizes.type_as(feats).view(-1, 1)
                feats = feats.contiguous()

        return feats, coords, sizes

    # @torch.no_grad()
    # def voxelize(self, points):
    #     total_start = time.time()
    #
    #     feats, coords, sizes = [], [], []
    #     for k, res in enumerate(points):
    #         loop_start = time.time()
    #
    #         # Processing each point cloud
    #         ret = self.pts_voxel_layer(res)
    #         if len(ret) == 3:
    #             # Hard voxelize
    #             f, c, n = ret
    #         else:
    #             assert len(ret) == 2
    #             f, c = ret
    #             n = None
    #         feats.append(f)
    #         coords.append(F.pad(c, (1, 0), mode='constant', value=k))
    #         if n is not None:
    #             sizes.append(n)
    #
    #         loop_end = time.time()
    #         print(f"Time for processing point cloud {k}: {loop_end - loop_start:.4f} seconds")
    #
    #     concat_start = time.time()
    #     feats = torch.cat(feats, dim=0)
    #     coords = torch.cat(coords, dim=0)
    #
    #     if len(sizes) > 0:
    #         sizes = torch.cat(sizes, dim=0)
    #         if self.voxelize_reduce:
    #             reduce_start = time.time()
    #             feats = feats.sum(dim=1, keepdim=False) / sizes.type_as(feats).view(-1, 1)
    #             feats = feats.contiguous()
    #             reduce_end = time.time()
    #             print(f"Time for voxelize reduction: {reduce_end - reduce_start:.4f} seconds")
    #
    #     concat_end = time.time()
    #     print(f"Time for concatenation: {concat_end - concat_start:.4f} seconds")
    #
    #     total_end = time.time()
    #     print(f"Total time for voxelize function: {total_end - total_start:.4f} seconds")
    #
    #     return feats, coords, sizes

    #***START_NO_AUTOCAST***
    # def predict(self, batch_inputs_dict: Dict[str, Optional[Tensor]],  # Original
    #             batch_data_samples: List[Det3DDataSample],
    #             **kwargs) -> List[Det3DDataSample]:
    #
    #     batch_input_metas = [item.metainfo for item in batch_data_samples]
    #     feats = self.extract_feat(batch_inputs_dict, batch_input_metas)
    #
    #     if self.with_bbox_head:
    #         outputs = self.bbox_head.predict(feats, batch_input_metas)
    #
    #     res = self.add_pred_to_datasample(batch_data_samples, outputs)
    #
    #     return res

    #***END_NO_AUTOCAST***

    # # ***START_AUTOCAST***
    def predict(self, batch_inputs_dict: Dict[str, Optional[Tensor]], #run bevfusion with autocast
                batch_data_samples: List[Det3DDataSample],
                **kwargs) -> List[Det3DDataSample]:

        # # Log the total number of LiDAR points before processing
        # points = batch_inputs_dict.get('points', [])
        # total_points = sum([p.shape[0] for p in points])
        # print(f"Total number of points processed: {total_points}")

        with torch.no_grad(), autocast():
            batch_input_metas = [item.metainfo for item in batch_data_samples]
            feats = self.extract_feat(batch_inputs_dict, batch_input_metas)

            if self.with_bbox_head:
                outputs = self.bbox_head.predict(feats, batch_input_metas)

            res = self.add_pred_to_datasample(batch_data_samples, outputs)

        return res
    # # ***END_AUTOCAST***

    def extract_feat(
            self,
            batch_inputs_dict,
            batch_input_metas,
            **kwargs,
    ):
        imgs = batch_inputs_dict.get('imgs', None)
        points = batch_inputs_dict.get('points', None)
        features = []
        if imgs is not None:
            imgs = imgs.contiguous()
            lidar2image, camera_intrinsics, camera2lidar = [], [], []
            img_aug_matrix, lidar_aug_matrix = [], []
            for i, meta in enumerate(batch_input_metas):
                lidar2image.append(meta['lidar2img'])
                camera_intrinsics.append(meta['cam2img'])
                camera2lidar.append(meta['cam2lidar'])
                img_aug_matrix.append(meta.get('img_aug_matrix', np.eye(4)))
                lidar_aug_matrix.append(
                    meta.get('lidar_aug_matrix', np.eye(4)))

            lidar2image = imgs.new_tensor(np.asarray(lidar2image))
            camera_intrinsics = imgs.new_tensor(np.array(camera_intrinsics))
            camera2lidar = imgs.new_tensor(np.asarray(camera2lidar))
            img_aug_matrix = imgs.new_tensor(np.asarray(img_aug_matrix))
            lidar_aug_matrix = imgs.new_tensor(np.asarray(lidar_aug_matrix))
            # img_feature = self.extract_img_feat(imgs, deepcopy(points),
            #                                      lidar2image, camera_intrinsics,
            #                                      camera2lidar, img_aug_matrix,
            #                                      lidar_aug_matrix,
            #                                      batch_input_metas)
            # Add visualization code for `img_feature`
            #self.summarize_tensor(img_feature)
            # self.visualize_all_channels(img_feature)
            # Save camera stream feature for visualization
            # torch.save(img_feature, 'img_feature.pt')
            # print(f"Camera feature saved: Shape {img_feature.shape}")
            img_feature = torch.zeros([1, 80, 180, 180])
            # # print(img_feature)
            img_feature = img_feature.to('cuda')
            features.append(img_feature)



        pts_feature = self.extract_pts_feat(batch_inputs_dict)
        # torch.save(pts_feature, 'pts_feature.pt')
        # print(f"LiDAR feature saved: Shape {pts_feature.shape}")
        features.append(pts_feature)


        if self.fusion_layer is not None:
            x = self.fusion_layer(features)
        else:
            assert len(features) == 1, features
            x = features[0]

        x = self.pts_backbone(x)
        x = self.pts_neck(x)

        return x

    def loss(self, batch_inputs_dict: Dict[str, Optional[Tensor]],
             batch_data_samples: List[Det3DDataSample],
             **kwargs) -> List[Det3DDataSample]:
        batch_input_metas = [item.metainfo for item in batch_data_samples]
        feats = self.extract_feat(batch_inputs_dict, batch_input_metas)

        losses = dict()
        if self.with_bbox_head:
            bbox_loss = self.bbox_head.loss(feats, batch_data_samples)

        losses.update(bbox_loss)

        return losses



    def summarize_tensor(self, tensor: torch.Tensor):
        """
        Prints summary statistics of a tensor.
        """
        print(f"Tensor Shape: {tensor.shape}")
        if tensor.dim() == 5:  # [B, N, C, H, W]
            batch, views, channels, height, width = tensor.shape
            tensor = tensor.view(batch * views, channels, height, width)
        elif tensor.dim() == 4:  # [B, C, H, W]
            batch, channels, height, width = tensor.shape
        else:
            raise ValueError(f"Unexpected tensor shape: {tensor.shape}")

        # Compute per-channel statistics
        stats = []
        for i in range(tensor.size(1)):  # Loop over channels
            channel = tensor[:, i, :, :].detach().cpu().numpy()
            stats.append({
                'channel': i,
                'mean': channel.mean(),
                'std': channel.std(),
                'min': channel.min(),
                'max': channel.max()
            })

        # Print stats
        for stat in stats:
            print(f"Channel {stat['channel']:02}: Mean={stat['mean']:.4f}, "
                  f"Std={stat['std']:.4f}, Min={stat['min']:.4f}, Max={stat['max']:.4f}")


    def visualize_all_channels(self, tensor: torch.Tensor, grid_size: int = 8):
        """
        Visualizes all channels of a tensor in a grid layout.

        Args:
            tensor (torch.Tensor): Input tensor with shape [B, C, H, W].
            grid_size (int): Number of columns in the grid.
        """
        print(f"Visualizing tensor of shape {tensor.shape}")
        tensor = tensor[0].detach().cpu()  # Take the first batch
        channels, height, width = tensor.shape

        # Set grid dimensions
        rows = (channels + grid_size - 1) // grid_size
        fig, axes = plt.subplots(rows, grid_size, figsize=(grid_size * 3, rows * 3))

        for i, ax in enumerate(axes.flat):
            if i < channels:
                channel_data = tensor[i].numpy()
                normalized_data = (channel_data - channel_data.min()) / (channel_data.max() - channel_data.min())
                ax.imshow(normalized_data, cmap='hot')
                ax.set_title(f'Channel {i}')
                ax.axis('off')
            else:
                ax.axis('off')  # Hide unused subplots

        plt.tight_layout()
        plt.show()

    def visualize_feature(self, feature: torch.Tensor, num_channels: int = 4, title="Feature Map"):
        """
        Visualizes the feature tensor as heatmaps for the first `num_channels` channels.

        Args:
            feature (torch.Tensor): The feature tensor, e.g., [B, C, H, W].
            num_channels (int): Number of channels to visualize.
            title (str): Title for the plot.
        """
        # Print the tensor shape
        print(f"{title} - Shape: {feature.shape}")

        # Take the first batch
        feature = feature[0].detach().cpu()

        # Visualize the first `num_channels` channels
        channels_to_visualize = min(feature.size(0), num_channels)
        fig, axes = plt.subplots(1, channels_to_visualize, figsize=(15, 5))

        for i in range(channels_to_visualize):
            channel_data = feature[i].numpy()
            normalized_data = (channel_data - channel_data.min()) / (channel_data.max() - channel_data.min())
            axes[i].imshow(normalized_data, cmap='hot')
            axes[i].set_title(f'Channel {i}')
            axes[i].axis('off')

        plt.suptitle(title)
        plt.tight_layout()
        plt.show()