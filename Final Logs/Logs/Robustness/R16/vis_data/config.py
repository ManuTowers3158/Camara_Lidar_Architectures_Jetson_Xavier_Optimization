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
custom_hooks = [
    dict(disable_after_epoch=15, type='DisableObjectSampleHook'),
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
data_root = '/media/geisler/A4ECA10AECA0D7B6/robustness/'
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
    data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
    info_path=
    '/media/geisler/A4ECA10AECA0D7B6/robustness/nuscenes_dbinfos_train.pkl',
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
    checkpoint=dict(interval=5, type='CheckpointHook'),
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
input_modality = dict(use_camera=False, use_lidar=True)
launcher = 'none'
load_from = 'projects/BEVFusion/configs/MMCV_Lidar_own.pth'
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
        pad_size_divisor=32,
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
    type='BEVFusion')
optim_wrapper = dict(
    clip_grad=dict(max_norm=35, norm_type=2),
    optimizer=dict(lr=0.0001, type='AdamW', weight_decay=0.01),
    type='OptimWrapper')
param_scheduler = [
    dict(
        T_max=8,
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=8,
        eta_min=0.001,
        type='CosineAnnealingLR'),
    dict(
        T_max=12,
        begin=8,
        by_epoch=True,
        convert_to_iter_based=True,
        end=20,
        eta_min=1e-08,
        type='CosineAnnealingLR'),
    dict(
        T_max=8,
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=8,
        eta_min=0.8947368421052632,
        type='CosineAnnealingMomentum'),
    dict(
        T_max=12,
        begin=8,
        by_epoch=True,
        convert_to_iter_based=True,
        end=20,
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
        data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
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
        modality=dict(use_camera=False, use_lidar=True),
        pipeline=[
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
            dict(type='PointShuffle'),
            dict(num_points=125000, type='PointSample'),
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
                    'num_views',
                ],
                type='Pack3DDetInputs'),
        ],
        test_mode=True,
        type='NuScenesDataset'),
    drop_last=False,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = dict(
    ann_file=
    '/media/geisler/A4ECA10AECA0D7B6/robustness/nuscenes_infos_val.pkl',
    backend_args=None,
    data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
    metric='bbox',
    type='NuScenesMetric')
test_pipeline = [
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
    dict(type='PointShuffle'),
    dict(num_points=125000, type='PointSample'),
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
            'num_views',
        ],
        type='Pack3DDetInputs'),
]
train_cfg = dict(by_epoch=True, max_epochs=20, val_interval=5)
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
            data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
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
            modality=dict(use_camera=False, use_lidar=True),
            pipeline=[
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
                dict(type='PointShuffle'),
                dict(num_points=125000, type='PointSample'),
                dict(
                    type='LoadAnnotations3D',
                    with_attr_label=False,
                    with_bbox_3d=True,
                    with_label_3d=True),
                dict(
                    db_sampler=dict(
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
                        data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
                        info_path=
                        '/media/geisler/A4ECA10AECA0D7B6/robustness/nuscenes_dbinfos_train.pkl',
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
                            truck=3)),
                    type='ObjectSample'),
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
                    type='GlobalRotScaleTrans'),
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
    dict(type='PointShuffle'),
    dict(num_points=125000, type='PointSample'),
    dict(
        type='LoadAnnotations3D',
        with_attr_label=False,
        with_bbox_3d=True,
        with_label_3d=True),
    dict(
        db_sampler=dict(
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
            data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
            info_path=
            '/media/geisler/A4ECA10AECA0D7B6/robustness/nuscenes_dbinfos_train.pkl',
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
                truck=3)),
        type='ObjectSample'),
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
        type='GlobalRotScaleTrans'),
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
        data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
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
        modality=dict(use_camera=False, use_lidar=True),
        pipeline=[
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
            dict(type='PointShuffle'),
            dict(num_points=125000, type='PointSample'),
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
                    'num_views',
                ],
                type='Pack3DDetInputs'),
        ],
        test_mode=True,
        type='NuScenesDataset'),
    drop_last=False,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = dict(
    ann_file=
    '/media/geisler/A4ECA10AECA0D7B6/robustness/nuscenes_infos_val.pkl',
    backend_args=None,
    data_root='/media/geisler/A4ECA10AECA0D7B6/robustness/',
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
work_dir = './work_dirs/bevfusion_lidar_voxel0075_125k'
