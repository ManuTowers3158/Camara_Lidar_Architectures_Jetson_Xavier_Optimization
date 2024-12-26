auto_scale_lr = dict(base_batch_size=32, enable=False)
backend_args = None
class_names = [
    'car',
    'truck',
    'construction_vehicle',
    'bus',
    'trailer',
    'barrier',
    'motorcycle',
    'bicycle',
    'pedestrian',
    'traffic_cone',
]
custom_imports = dict(
    allow_failed_imports=False, imports=[
        'projects.BEVFusion.bevfusion',
    ])
data_prefix = dict(
    CAM_BACK='samples/CAM_BACK',
    CAM_BACK_LEFT='samples/CAM_BACK_LEFT',
    CAM_BACK_RIGHT='samples/CAM_BACK_RIGHT',
    CAM_FRONT='samples/CAM_FRONT',
    CAM_FRONT_LEFT='samples/CAM_FRONT_LEFT',
    CAM_FRONT_RIGHT='samples/CAM_FRONT_RIGHT',
    pts='samples/LIDAR_TOP',
    sweeps='sweeps/LIDAR_TOP')
data_root = '/media/xavier02/Sparkles1/nuscenes/'
dataset_type = 'NuScenesDataset'
db_sampler = dict(
    classes=[
        'car',
        'truck',
        'construction_vehicle',
        'bus',
        'trailer',
        'barrier',
        'motorcycle',
        'bicycle',
        'pedestrian',
        'traffic_cone',
    ],
    data_root='/media/xavier02/Sparkles1/nuscenes/',
    info_path='/media/xavier02/Sparkles1/nuscenes/nuscenes_dbinfos_train.pkl',
    points_loader=dict(
        backend_args=None,
        coord_type='LIDAR',
        load_dim=5,
        type='LoadPointsFromFile',
        use_dim=[
            0,
            1,
            2,
            3,
            4,
        ]),
    prepare=dict(
        filter_by_difficulty=[
            -1,
        ],
        filter_by_min_points=dict(
            barrier=5,
            bicycle=5,
            bus=5,
            car=5,
            construction_vehicle=5,
            motorcycle=5,
            pedestrian=5,
            traffic_cone=5,
            trailer=5,
            truck=5)),
    rate=1.0,
    sample_groups=dict(
        barrier=2,
        bicycle=6,
        bus=4,
        car=2,
        construction_vehicle=7,
        motorcycle=6,
        pedestrian=2,
        traffic_cone=2,
        trailer=6,
        truck=3))
default_hooks = dict(
    checkpoint=dict(interval=1, type='CheckpointHook'),
    logger=dict(interval=50, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(type='Det3DVisualizationHook'))
default_scope = 'mmdet3d'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
input_modality = dict(use_camera=True, use_lidar=True)
launcher = 'none'
load_from = '/media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_Lidar_wResnet18_checkpoint.pth'
log_level = 'INFO'
log_processor = dict(by_epoch=True, type='LogProcessor', window_size=50)
lr = 0.0001
metainfo = dict(classes=[
    'car',
    'truck',
    'construction_vehicle',
    'bus',
    'trailer',
    'barrier',
    'motorcycle',
    'bicycle',
    'pedestrian',
    'traffic_cone',
])
model = dict(
    bbox_head=dict(
        auxiliary=True,
        bbox_coder=dict(
            code_size=10,
            out_size_factor=8,
            pc_range=[
                -54.0,
                -54.0,
            ],
            post_center_range=[
                -61.2,
                -61.2,
                -10.0,
                61.2,
                61.2,
                10.0,
            ],
            score_threshold=0.0,
            type='TransFusionBBoxCoder',
            voxel_size=[
                0.075,
                0.075,
            ]),
        bn_momentum=0.1,
        common_heads=dict(
            center=[
                2,
                2,
            ],
            dim=[
                3,
                2,
            ],
            height=[
                1,
                2,
            ],
            rot=[
                2,
                2,
            ],
            vel=[
                2,
                2,
            ]),
        decoder_layer=dict(
            cross_attn_cfg=dict(dropout=0.1, embed_dims=128, num_heads=8),
            ffn_cfg=dict(
                act_cfg=dict(inplace=True, type='ReLU'),
                embed_dims=128,
                feedforward_channels=256,
                ffn_drop=0.1,
                num_fcs=2),
            norm_cfg=dict(type='LN'),
            pos_encoding_cfg=dict(input_channel=2, num_pos_feats=128),
            self_attn_cfg=dict(dropout=0.1, embed_dims=128, num_heads=8),
            type='TransformerDecoderLayer'),
        hidden_channel=128,
        in_channels=512,
        loss_bbox=dict(
            loss_weight=0.25, reduction='mean', type='mmdet.L1Loss'),
        loss_cls=dict(
            alpha=0.25,
            gamma=2.0,
            loss_weight=1.0,
            reduction='mean',
            type='mmdet.FocalLoss',
            use_sigmoid=True),
        loss_heatmap=dict(
            loss_weight=1.0, reduction='mean', type='mmdet.GaussianFocalLoss'),
        nms_kernel_size=3,
        num_classes=10,
        num_decoder_layers=1,
        num_proposals=200,
        test_cfg=dict(
            dataset='nuScenes',
            grid_size=[
                1440,
                1440,
                41,
            ],
            nms_type=None,
            out_size_factor=8,
            pc_range=[
                -54.0,
                -54.0,
            ],
            voxel_size=[
                0.075,
                0.075,
            ]),
        train_cfg=dict(
            assigner=dict(
                cls_cost=dict(
                    alpha=0.25,
                    gamma=2.0,
                    type='mmdet.FocalLossCost',
                    weight=0.15),
                iou_calculator=dict(coordinate='lidar', type='BboxOverlaps3D'),
                iou_cost=dict(type='IoU3DCost', weight=0.25),
                reg_cost=dict(type='BBoxBEVL1Cost', weight=0.25),
                type='HungarianAssigner3D'),
            code_weights=[
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.2,
                0.2,
            ],
            dataset='nuScenes',
            gaussian_overlap=0.1,
            grid_size=[
                1440,
                1440,
                41,
            ],
            min_radius=2,
            out_size_factor=8,
            point_cloud_range=[
                -54.0,
                -54.0,
                -5.0,
                54.0,
                54.0,
                3.0,
            ],
            pos_weight=-1,
            voxel_size=[
                0.075,
                0.075,
                0.2,
            ]),
        type='TransFusionHead'),
    data_preprocessor=dict(
        bgr_to_rgb=False,
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        pad_size_divisor=32,
        std=[
            58.395,
            57.12,
            57.375,
        ],
        type='Det3DDataPreprocessor',
        voxelize_cfg=dict(
            max_num_points=10,
            max_voxels=[
                120000,
                160000,
            ],
            point_cloud_range=[
                -54.0,
                -54.0,
                -5.0,
                54.0,
                54.0,
                3.0,
            ],
            voxel_size=[
                0.075,
                0.075,
                0.2,
            ],
            voxelize_reduce=True)),
    fusion_layer=dict(
        in_channels=[
            80,
            256,
        ], out_channels=256, type='ConvFuser'),
    img_backbone=dict(
        depth=18,
        frozen_stages=1,
        init_cfg=dict(
            checkpoint=
            '/media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/resnet18.pth',
            type='Pretrained'),
        norm_cfg=dict(requires_grad=True, type='BN'),
        norm_eval=True,
        num_stages=4,
        out_indices=(
            0,
            1,
            2,
            3,
        ),
        style='pytorch',
        type='mmdet.ResNet'),
    img_neck=dict(
        act_cfg=dict(inplace=True, type='ReLU'),
        in_channels=[
            64,
            128,
            256,
            512,
        ],
        norm_cfg=dict(requires_grad=True, type='BN2d'),
        num_outs=3,
        out_channels=256,
        start_level=0,
        type='GeneralizedLSSFPN_2',
        upsample_cfg=dict(align_corners=False, mode='bilinear')),
    pts_backbone=dict(
        conv_cfg=dict(bias=False, type='Conv2d'),
        in_channels=256,
        layer_nums=[
            5,
            5,
        ],
        layer_strides=[
            1,
            2,
        ],
        norm_cfg=dict(eps=0.001, momentum=0.01, type='BN'),
        out_channels=[
            128,
            256,
        ],
        type='SECOND'),
    pts_middle_encoder=dict(
        block_type='basicblock',
        encoder_channels=(
            (
                16,
                16,
                32,
            ),
            (
                32,
                32,
                64,
            ),
            (
                64,
                64,
                128,
            ),
            (
                128,
                128,
            ),
        ),
        encoder_paddings=(
            (
                0,
                0,
                1,
            ),
            (
                0,
                0,
                1,
            ),
            (
                0,
                0,
                (
                    1,
                    1,
                    0,
                ),
            ),
            (
                0,
                0,
            ),
        ),
        in_channels=5,
        norm_cfg=dict(eps=0.001, momentum=0.01, type='BN1d'),
        order=(
            'conv',
            'norm',
            'act',
        ),
        sparse_shape=[
            1440,
            1440,
            41,
        ],
        type='BEVFusionSparseEncoder'),
    pts_neck=dict(
        in_channels=[
            128,
            256,
        ],
        norm_cfg=dict(eps=0.001, momentum=0.01, type='BN'),
        out_channels=[
            256,
            256,
        ],
        type='SECONDFPN',
        upsample_cfg=dict(bias=False, type='deconv'),
        upsample_strides=[
            1,
            2,
        ],
        use_conv_for_no_stride=True),
    pts_voxel_encoder=dict(num_features=5, type='HardSimpleVFE'),
    type='BEVFusion',
    view_transform=dict(
        dbound=[
            1.0,
            60.0,
            0.5,
        ],
        downsample=2,
        feature_size=[
            32,
            88,
        ],
        image_size=[
            256,
            704,
        ],
        in_channels=256,
        out_channels=80,
        type='DepthLSSTransform',
        xbound=[
            -54.0,
            54.0,
            0.3,
        ],
        ybound=[
            -54.0,
            54.0,
            0.3,
        ],
        zbound=[
            -10.0,
            10.0,
            20.0,
        ]))
optim_wrapper = dict(
    clip_grad=dict(max_norm=35, norm_type=2),
    optimizer=dict(lr=0.0002, type='AdamW', weight_decay=0.01),
    type='OptimWrapper')
param_scheduler = [
    dict(
        begin=0,
        by_epoch=False,
        end=500,
        start_factor=0.33333333,
        type='LinearLR'),
    dict(
        T_max=6,
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=6,
        eta_min_ratio=0.0001,
        type='CosineAnnealingLR'),
    dict(
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=2.4,
        eta_min=0.8947368421052632,
        type='CosineAnnealingMomentum'),
    dict(
        begin=2.4,
        by_epoch=True,
        convert_to_iter_based=True,
        end=6,
        eta_min=1,
        type='CosineAnnealingMomentum'),
]
point_cloud_range = [
    -54.0,
    -54.0,
    -5.0,
    54.0,
    54.0,
    3.0,
]
resume = False
test_cfg = dict()
test_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='nuscenes_infos_val.pkl',
        backend_args=None,
        box_type_3d='LiDAR',
        data_prefix=dict(
            CAM_BACK='samples/CAM_BACK',
            CAM_BACK_LEFT='samples/CAM_BACK_LEFT',
            CAM_BACK_RIGHT='samples/CAM_BACK_RIGHT',
            CAM_FRONT='samples/CAM_FRONT',
            CAM_FRONT_LEFT='samples/CAM_FRONT_LEFT',
            CAM_FRONT_RIGHT='samples/CAM_FRONT_RIGHT',
            pts='samples/LIDAR_TOP',
            sweeps='sweeps/LIDAR_TOP'),
        data_root='/media/xavier02/Sparkles1/nuscenes/',
        metainfo=dict(classes=[
            'car',
            'truck',
            'construction_vehicle',
            'bus',
            'trailer',
            'barrier',
            'motorcycle',
            'bicycle',
            'pedestrian',
            'traffic_cone',
        ]),
        modality=dict(use_camera=True, use_lidar=True),
        pipeline=[
            dict(
                backend_args=None,
                color_type='color',
                to_float32=True,
                type='BEVLoadMultiViewImageFromFiles'),
            dict(
                backend_args=None,
                coord_type='LIDAR',
                load_dim=5,
                type='LoadPointsFromFile',
                use_dim=5),
            dict(
                backend_args=None,
                load_dim=5,
                pad_empty_sweeps=True,
                remove_close=True,
                sweeps_num=9,
                type='LoadPointsFromMultiSweeps',
                use_dim=5),
            dict(
                bot_pct_lim=[
                    0.0,
                    0.0,
                ],
                final_dim=[
                    256,
                    704,
                ],
                is_train=False,
                rand_flip=False,
                resize_lim=[
                    0.48,
                    0.48,
                ],
                rot_lim=[
                    0.0,
                    0.0,
                ],
                type='ImageAug3D'),
            dict(
                point_cloud_range=[
                    -54.0,
                    -54.0,
                    -5.0,
                    54.0,
                    54.0,
                    3.0,
                ],
                type='PointsRangeFilter'),
            dict(
                keys=[
                    'img',
                    'points',
                    'gt_bboxes_3d',
                    'gt_labels_3d',
                ],
                meta_keys=[
                    'cam2img',
                    'ori_cam2img',
                    'lidar2cam',
                    'lidar2img',
                    'cam2lidar',
                    'ori_lidar2img',
                    'img_aug_matrix',
                    'box_type_3d',
                    'sample_idx',
                    'lidar_path',
                    'img_path',
                    'num_pts_feats',
                ],
                type='Pack3DDetInputs'),
        ],
        test_mode=True,
        type='NuScenesDataset'),
    drop_last=False,
    num_workers=1,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    ann_file='/media/xavier02/Sparkles1/nuscenes/nuscenes_infos_val.pkl',
    backend_args=None,
    data_root='/media/xavier02/Sparkles1/nuscenes/',
    metric='bbox',
    type='NuScenesMetric')
test_pipeline = [
    dict(
        backend_args=None,
        color_type='color',
        to_float32=True,
        type='BEVLoadMultiViewImageFromFiles'),
    dict(
        backend_args=None,
        coord_type='LIDAR',
        load_dim=5,
        type='LoadPointsFromFile',
        use_dim=5),
    dict(
        backend_args=None,
        load_dim=5,
        pad_empty_sweeps=True,
        remove_close=True,
        sweeps_num=9,
        type='LoadPointsFromMultiSweeps',
        use_dim=5),
    dict(
        bot_pct_lim=[
            0.0,
            0.0,
        ],
        final_dim=[
            256,
            704,
        ],
        is_train=False,
        rand_flip=False,
        resize_lim=[
            0.48,
            0.48,
        ],
        rot_lim=[
            0.0,
            0.0,
        ],
        type='ImageAug3D'),
    dict(
        point_cloud_range=[
            -54.0,
            -54.0,
            -5.0,
            54.0,
            54.0,
            3.0,
        ],
        type='PointsRangeFilter'),
    dict(
        keys=[
            'img',
            'points',
            'gt_bboxes_3d',
            'gt_labels_3d',
        ],
        meta_keys=[
            'cam2img',
            'ori_cam2img',
            'lidar2cam',
            'lidar2img',
            'cam2lidar',
            'ori_lidar2img',
            'img_aug_matrix',
            'box_type_3d',
            'sample_idx',
            'lidar_path',
            'img_path',
            'num_pts_feats',
        ],
        type='Pack3DDetInputs'),
]
train_cfg = dict(by_epoch=True, max_epochs=6, val_interval=1)
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        dataset=dict(
            ann_file='nuscenes_infos_train.pkl',
            box_type_3d='LiDAR',
            data_prefix=dict(
                CAM_BACK='samples/CAM_BACK',
                CAM_BACK_LEFT='samples/CAM_BACK_LEFT',
                CAM_BACK_RIGHT='samples/CAM_BACK_RIGHT',
                CAM_FRONT='samples/CAM_FRONT',
                CAM_FRONT_LEFT='samples/CAM_FRONT_LEFT',
                CAM_FRONT_RIGHT='samples/CAM_FRONT_RIGHT',
                pts='samples/LIDAR_TOP',
                sweeps='sweeps/LIDAR_TOP'),
            data_root='/media/xavier02/Sparkles1/nuscenes/',
            metainfo=dict(classes=[
                'car',
                'truck',
                'construction_vehicle',
                'bus',
                'trailer',
                'barrier',
                'motorcycle',
                'bicycle',
                'pedestrian',
                'traffic_cone',
            ]),
            modality=dict(use_camera=True, use_lidar=True),
            pipeline=[
                dict(
                    backend_args=None,
                    color_type='color',
                    to_float32=True,
                    type='BEVLoadMultiViewImageFromFiles'),
                dict(
                    backend_args=None,
                    coord_type='LIDAR',
                    load_dim=5,
                    type='LoadPointsFromFile',
                    use_dim=5),
                dict(
                    backend_args=None,
                    load_dim=5,
                    pad_empty_sweeps=True,
                    remove_close=True,
                    sweeps_num=9,
                    type='LoadPointsFromMultiSweeps',
                    use_dim=5),
                dict(
                    type='LoadAnnotations3D',
                    with_attr_label=False,
                    with_bbox_3d=True,
                    with_label_3d=True),
                dict(
                    bot_pct_lim=[
                        0.0,
                        0.0,
                    ],
                    final_dim=[
                        256,
                        704,
                    ],
                    is_train=True,
                    rand_flip=True,
                    resize_lim=[
                        0.38,
                        0.55,
                    ],
                    rot_lim=[
                        -5.4,
                        5.4,
                    ],
                    type='ImageAug3D'),
                dict(
                    rot_range=[
                        -0.78539816,
                        0.78539816,
                    ],
                    scale_ratio_range=[
                        0.9,
                        1.1,
                    ],
                    translation_std=0.5,
                    type='BEVFusionGlobalRotScaleTrans'),
                dict(type='BEVFusionRandomFlip3D'),
                dict(
                    point_cloud_range=[
                        -54.0,
                        -54.0,
                        -5.0,
                        54.0,
                        54.0,
                        3.0,
                    ],
                    type='PointsRangeFilter'),
                dict(
                    point_cloud_range=[
                        -54.0,
                        -54.0,
                        -5.0,
                        54.0,
                        54.0,
                        3.0,
                    ],
                    type='ObjectRangeFilter'),
                dict(
                    classes=[
                        'car',
                        'truck',
                        'construction_vehicle',
                        'bus',
                        'trailer',
                        'barrier',
                        'motorcycle',
                        'bicycle',
                        'pedestrian',
                        'traffic_cone',
                    ],
                    type='ObjectNameFilter'),
                dict(
                    fixed_prob=True,
                    max_epoch=6,
                    mode=1,
                    offset=False,
                    prob=0.0,
                    ratio=0.5,
                    rotate=1,
                    type='GridMask',
                    use_h=True,
                    use_w=True),
                dict(type='PointShuffle'),
                dict(
                    keys=[
                        'points',
                        'img',
                        'gt_bboxes_3d',
                        'gt_labels_3d',
                        'gt_bboxes',
                        'gt_labels',
                    ],
                    meta_keys=[
                        'cam2img',
                        'ori_cam2img',
                        'lidar2cam',
                        'lidar2img',
                        'cam2lidar',
                        'ori_lidar2img',
                        'img_aug_matrix',
                        'box_type_3d',
                        'sample_idx',
                        'lidar_path',
                        'img_path',
                        'transformation_3d_flow',
                        'pcd_rotation',
                        'pcd_scale_factor',
                        'pcd_trans',
                        'img_aug_matrix',
                        'lidar_aug_matrix',
                        'num_pts_feats',
                    ],
                    type='Pack3DDetInputs'),
            ],
            test_mode=False,
            type='NuScenesDataset',
            use_valid_flag=True),
        type='CBGSDataset'),
    num_workers=1,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(
        backend_args=None,
        color_type='color',
        to_float32=True,
        type='BEVLoadMultiViewImageFromFiles'),
    dict(
        backend_args=None,
        coord_type='LIDAR',
        load_dim=5,
        type='LoadPointsFromFile',
        use_dim=5),
    dict(
        backend_args=None,
        load_dim=5,
        pad_empty_sweeps=True,
        remove_close=True,
        sweeps_num=9,
        type='LoadPointsFromMultiSweeps',
        use_dim=5),
    dict(
        type='LoadAnnotations3D',
        with_attr_label=False,
        with_bbox_3d=True,
        with_label_3d=True),
    dict(
        bot_pct_lim=[
            0.0,
            0.0,
        ],
        final_dim=[
            256,
            704,
        ],
        is_train=True,
        rand_flip=True,
        resize_lim=[
            0.38,
            0.55,
        ],
        rot_lim=[
            -5.4,
            5.4,
        ],
        type='ImageAug3D'),
    dict(
        rot_range=[
            -0.78539816,
            0.78539816,
        ],
        scale_ratio_range=[
            0.9,
            1.1,
        ],
        translation_std=0.5,
        type='BEVFusionGlobalRotScaleTrans'),
    dict(type='BEVFusionRandomFlip3D'),
    dict(
        point_cloud_range=[
            -54.0,
            -54.0,
            -5.0,
            54.0,
            54.0,
            3.0,
        ],
        type='PointsRangeFilter'),
    dict(
        point_cloud_range=[
            -54.0,
            -54.0,
            -5.0,
            54.0,
            54.0,
            3.0,
        ],
        type='ObjectRangeFilter'),
    dict(
        classes=[
            'car',
            'truck',
            'construction_vehicle',
            'bus',
            'trailer',
            'barrier',
            'motorcycle',
            'bicycle',
            'pedestrian',
            'traffic_cone',
        ],
        type='ObjectNameFilter'),
    dict(
        fixed_prob=True,
        max_epoch=6,
        mode=1,
        offset=False,
        prob=0.0,
        ratio=0.5,
        rotate=1,
        type='GridMask',
        use_h=True,
        use_w=True),
    dict(type='PointShuffle'),
    dict(
        keys=[
            'points',
            'img',
            'gt_bboxes_3d',
            'gt_labels_3d',
            'gt_bboxes',
            'gt_labels',
        ],
        meta_keys=[
            'cam2img',
            'ori_cam2img',
            'lidar2cam',
            'lidar2img',
            'cam2lidar',
            'ori_lidar2img',
            'img_aug_matrix',
            'box_type_3d',
            'sample_idx',
            'lidar_path',
            'img_path',
            'transformation_3d_flow',
            'pcd_rotation',
            'pcd_scale_factor',
            'pcd_trans',
            'img_aug_matrix',
            'lidar_aug_matrix',
            'num_pts_feats',
        ],
        type='Pack3DDetInputs'),
]
val_cfg = dict()
val_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='nuscenes_infos_val.pkl',
        backend_args=None,
        box_type_3d='LiDAR',
        data_prefix=dict(
            CAM_BACK='samples/CAM_BACK',
            CAM_BACK_LEFT='samples/CAM_BACK_LEFT',
            CAM_BACK_RIGHT='samples/CAM_BACK_RIGHT',
            CAM_FRONT='samples/CAM_FRONT',
            CAM_FRONT_LEFT='samples/CAM_FRONT_LEFT',
            CAM_FRONT_RIGHT='samples/CAM_FRONT_RIGHT',
            pts='samples/LIDAR_TOP',
            sweeps='sweeps/LIDAR_TOP'),
        data_root='/media/xavier02/Sparkles1/nuscenes/',
        metainfo=dict(classes=[
            'car',
            'truck',
            'construction_vehicle',
            'bus',
            'trailer',
            'barrier',
            'motorcycle',
            'bicycle',
            'pedestrian',
            'traffic_cone',
        ]),
        modality=dict(use_camera=True, use_lidar=True),
        pipeline=[
            dict(
                backend_args=None,
                color_type='color',
                to_float32=True,
                type='BEVLoadMultiViewImageFromFiles'),
            dict(
                backend_args=None,
                coord_type='LIDAR',
                load_dim=5,
                type='LoadPointsFromFile',
                use_dim=5),
            dict(
                backend_args=None,
                load_dim=5,
                pad_empty_sweeps=True,
                remove_close=True,
                sweeps_num=9,
                type='LoadPointsFromMultiSweeps',
                use_dim=5),
            dict(
                bot_pct_lim=[
                    0.0,
                    0.0,
                ],
                final_dim=[
                    256,
                    704,
                ],
                is_train=False,
                rand_flip=False,
                resize_lim=[
                    0.48,
                    0.48,
                ],
                rot_lim=[
                    0.0,
                    0.0,
                ],
                type='ImageAug3D'),
            dict(
                point_cloud_range=[
                    -54.0,
                    -54.0,
                    -5.0,
                    54.0,
                    54.0,
                    3.0,
                ],
                type='PointsRangeFilter'),
            dict(
                keys=[
                    'img',
                    'points',
                    'gt_bboxes_3d',
                    'gt_labels_3d',
                ],
                meta_keys=[
                    'cam2img',
                    'ori_cam2img',
                    'lidar2cam',
                    'lidar2img',
                    'cam2lidar',
                    'ori_lidar2img',
                    'img_aug_matrix',
                    'box_type_3d',
                    'sample_idx',
                    'lidar_path',
                    'img_path',
                    'num_pts_feats',
                ],
                type='Pack3DDetInputs'),
        ],
        test_mode=True,
        type='NuScenesDataset'),
    drop_last=False,
    num_workers=1,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    ann_file='/media/xavier02/Sparkles1/nuscenes/nuscenes_infos_val.pkl',
    backend_args=None,
    data_root='/media/xavier02/Sparkles1/nuscenes/',
    metric='bbox',
    type='NuScenesMetric')
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='Det3DLocalVisualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
    ])
voxel_size = [
    0.075,
    0.075,
    0.2,
]
work_dir = './work_dirs/bevfusion_lidar-cam_voxel0075_second_with_resnet_18'
