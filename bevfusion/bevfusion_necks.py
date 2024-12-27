# modify from https://github.com/mit-han-lab/bevfusion
import torch
import torch.nn as nn
import torch.nn.functional as F
from mmcv.cnn import ConvModule
from mmengine.model import BaseModule

from mmdet3d.registry import MODELS


@MODELS.register_module()
class GeneralizedLSSFPN(BaseModule):

    def __init__(
            self,
            in_channels,
            out_channels,
            num_outs,
            start_level=0,
            end_level=-1,
            no_norm_on_lateral=False,
            conv_cfg=None,
            norm_cfg=dict(type='BN2d'),
            act_cfg=dict(type='ReLU'),
            upsample_cfg=dict(mode='bilinear', align_corners=True),
    ) -> None:
        super().__init__()
        assert isinstance(in_channels, list)
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.num_ins = len(in_channels)
        self.num_outs = num_outs
        self.no_norm_on_lateral = no_norm_on_lateral
        self.fp16_enabled = False
        self.upsample_cfg = upsample_cfg.copy()

        if end_level == -1:
            self.backbone_end_level = self.num_ins - 1
            # assert num_outs >= self.num_ins - start_level
        else:
            # if end_level < inputs, no extra level is allowed
            self.backbone_end_level = end_level
            assert end_level <= len(in_channels)
            assert num_outs == end_level - start_level
        self.start_level = start_level
        self.end_level = end_level

        self.lateral_convs = nn.ModuleList()
        self.fpn_convs = nn.ModuleList()

        for i in range(self.start_level, self.backbone_end_level):
            l_conv = ConvModule(
                in_channels[i] +
                (in_channels[i + 1] if i == self.backbone_end_level -
                 1 else out_channels),
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg if not self.no_norm_on_lateral else None,
                act_cfg=act_cfg,
                inplace=False,
            )
            fpn_conv = ConvModule(
                out_channels,
                out_channels,
                3,
                padding=1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
                inplace=False,
            )

            self.lateral_convs.append(l_conv)
            self.fpn_convs.append(fpn_conv)

    def forward(self, inputs):#********ORIGINAL FUNCTION****
        """Forward function."""
        # upsample -> cat -> conv1x1 -> conv3x3
        assert len(inputs) == len(self.in_channels)

        # build laterals
        laterals = [inputs[i + self.start_level] for i in range(len(inputs))]

        # build top-down path
        used_backbone_levels = len(laterals) - 1
        for i in range(used_backbone_levels - 1, -1, -1):
            x = F.interpolate(
                laterals[i + 1],
                size=laterals[i].shape[2:],
                **self.upsample_cfg,
            )
            laterals[i] = torch.cat([laterals[i], x], dim=1)
            laterals[i] = self.lateral_convs[i](laterals[i])
            laterals[i] = self.fpn_convs[i](laterals[i])

        # build outputs
        outs = [laterals[i] for i in range(used_backbone_levels)]
        return tuple(outs)

    # def forward(self, inputs): #*******original with debug
    #     """Forward function with print statements to display output sizes."""
    #     # Ensure the number of inputs matches the in_channels configuration
    #     assert len(inputs) == len(self.in_channels)
    #
    #     # Initial input sizes
    #     for idx, input_tensor in enumerate(inputs):
    #         print(f"Input size at level {idx}: {input_tensor.shape}")
    #
    #     # Build laterals
    #     laterals = [inputs[i + self.start_level] for i in range(len(inputs))]
    #
    #     # Output sizes after building the laterals
    #     for idx, lateral in enumerate(laterals):
    #         print(f"Lateral size at level {idx + self.start_level}: {lateral.shape}")
    #
    #     # Build top-down path
    #     used_backbone_levels = len(laterals) - 1
    #     for i in range(used_backbone_levels - 1, -1, -1):
    #         x = F.interpolate(
    #             laterals[i + 1],
    #             size=laterals[i].shape[2:],
    #             **self.upsample_cfg,
    #         )
    #         print(f"Interpolated size at level {i + 1}: {x.shape}")
    #
    #         laterals[i] = torch.cat([laterals[i], x], dim=1)
    #         print(f"Concatenated lateral size at level {i}: {laterals[i].shape}")
    #
    #         laterals[i] = self.lateral_convs[i](laterals[i])
    #         print(f"Lateral conv output size at level {i}: {laterals[i].shape}")
    #
    #         laterals[i] = self.fpn_convs[i](laterals[i])
    #         print(f"FPN conv output size at level {i}: {laterals[i].shape}")
    #
    #     # Build outputs
    #     outs = [laterals[i] for i in range(used_backbone_levels)]
    #
    #     # Output sizes at the end of each level
    #     for idx, out in enumerate(outs):
    #         print(f"Output size at level {idx}: {out.shape}")
    #
    #     return tuple(outs)



    # def forward(self, inputs): #******Official RESNET 50,34,18 Neck
    #     """Forward function for the neck."""
    #     assert len(inputs) == len(self.in_channels)
    #
    #     # Build laterals (initial feature maps from the backbone)
    #     laterals = [inputs[i + self.start_level] for i in range(len(inputs))]
    #
    #     # Resize the first map (e.g., from 64x176 to 32x88) before upsampling and merging
    #     laterals[0] = F.interpolate(laterals[0], size=(32, 88))  # Adjust the size as needed
    #
    #     # Build the top-down path (upsampling and merging)
    #     used_backbone_levels = len(laterals) - 1
    #     for i in range(used_backbone_levels - 1, -1, -1):
    #         x = F.interpolate(
    #             laterals[i + 1],
    #             size=laterals[i].shape[2:],  # Match the spatial size of the larger map
    #             **self.upsample_cfg,
    #         )
    #         laterals[i] = torch.cat([laterals[i], x], dim=1)  # Concatenate upsampled map
    #         laterals[i] = self.lateral_convs[i](laterals[i])
    #         laterals[i] = self.fpn_convs[i](laterals[i])
    #
    #     # Build final outputs
    #     outs = [laterals[i] for i in range(used_backbone_levels + 1)]
    #
    #     return tuple(outs)



@MODELS.register_module()
class GeneralizedLSSFPN_2(BaseModule):
    def __init__(
            self,
            in_channels,
            out_channels,
            num_outs,
            start_level=0,
            end_level=-1,
            no_norm_on_lateral=False,
            conv_cfg=None,
            norm_cfg=dict(type='BN2d'),
            act_cfg=dict(type='ReLU'),
            upsample_cfg=dict(mode='bilinear', align_corners=True),
    ) -> None:
        super().__init__()
        assert isinstance(in_channels, list)
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.num_ins = len(in_channels)
        self.num_outs = num_outs
        self.no_norm_on_lateral = no_norm_on_lateral
        self.fp16_enabled = False
        self.upsample_cfg = upsample_cfg.copy()

        if end_level == -1:
            self.backbone_end_level = self.num_ins - 1
            # assert num_outs >= self.num_ins - start_level
        else:
            # if end_level < inputs, no extra level is allowed
            self.backbone_end_level = end_level
            assert end_level <= len(in_channels)
            assert num_outs == end_level - start_level
        self.start_level = start_level
        self.end_level = end_level

        self.lateral_convs = nn.ModuleList()
        self.fpn_convs = nn.ModuleList()

        for i in range(self.start_level, self.backbone_end_level):
            l_conv = ConvModule(
                in_channels[i] +
                (in_channels[i + 1] if i == self.backbone_end_level -
                                       1 else out_channels),
                out_channels,
                1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg if not self.no_norm_on_lateral else None,
                act_cfg=act_cfg,
                inplace=False,
            )
            fpn_conv = ConvModule(
                out_channels,
                out_channels,
                3,
                padding=1,
                conv_cfg=conv_cfg,
                norm_cfg=norm_cfg,
                act_cfg=act_cfg,
                inplace=False,
            )

            self.lateral_convs.append(l_conv)
            self.fpn_convs.append(fpn_conv)

    def forward(self, inputs):  # ******Official RESNET 50,34,18 Neck
        """Forward function for the neck."""
        assert len(inputs) == len(self.in_channels)

        # Build laterals (initial feature maps from the backbone)
        laterals = [inputs[i + self.start_level] for i in range(len(inputs))]

        # Resize the first map (e.g., from 64x176 to 32x88) before upsampling and merging
        laterals[0] = F.interpolate(laterals[0], size=(32, 88))  # Adjust the size as needed

        # Build the top-down path (upsampling and merging)
        used_backbone_levels = len(laterals) - 1
        for i in range(used_backbone_levels - 1, -1, -1):
            x = F.interpolate(
                laterals[i + 1],
                size=laterals[i].shape[2:],  # Match the spatial size of the larger map
                **self.upsample_cfg,
            )
            laterals[i] = torch.cat([laterals[i], x], dim=1)  # Concatenate upsampled map
            laterals[i] = self.lateral_convs[i](laterals[i])
            laterals[i] = self.fpn_convs[i](laterals[i])

        # Build final outputs
        outs = [laterals[i] for i in range(used_backbone_levels + 1)]

        return tuple(outs)



