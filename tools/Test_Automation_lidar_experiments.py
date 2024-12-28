import os
import spconv
print(spconv.__version__)
# Sequence 1: Test lidar sweeps
command_1 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_9sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_2 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_8sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_3 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_7sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_4 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_6sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_5 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_5sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_6 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_4sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_7 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_3sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_8 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_2sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_9 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_1sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"


# Sequence 2: Test lidar points resolution
command_10 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_225k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_11 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_200k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_12 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_175k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_13 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_150k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_14 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_125k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_15 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_100k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_16 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_75k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_17 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_50k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"

# Sequence 3: Test cam lidar sweeps own checkpoint resnet18
command_18 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_1s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_19 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_2s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_20 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_3s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_21 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_4s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_22 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_5s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_23 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_6s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_24 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_7s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_25 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_8s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_26 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_9s_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"

# Sequence 4: Test cam lidar sweeps own checkpoint swin
command_27 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_1s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_28 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_2s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_29 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_3s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_30 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_4s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_31 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_5s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_32 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_6s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_33 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_7s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_34 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_8s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_35 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_9s_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"

# Sequence 5: Test cam lidar points density own checkpoint resnet
command_36 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_225k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_37 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_200k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_38 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_175k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_39 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_150k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_40 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_125k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_41 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_100k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_42 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_75k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_43 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_50k_resnet18.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"

# Sequence 6: Test cam lidar points density own checkpoint swin
command_44 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_50k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_45 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_75k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_46 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_100k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_47 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_125k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_48 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_150k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_49 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_175k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_50 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_200k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
command_51 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_225k_swin.py projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"



# Function to run a command N times
def run_command(command, times):
    for i in range(times):
        print(f"Running iteration {i+1} of command: {command}")
        os.system(command)

# Run the commands 10 times each
# run_command(command_1, 1)
# run_command(command_2, 1)
# run_command(command_3, 1)
# run_command(command_4, 1)
# run_command(command_5, 1)
# run_command(command_6, 1)
# run_command(command_7, 1)
# run_command(command_8, 1)
# run_command(command_9, 1)
#
# run_command(command_10, 1)
# run_command(command_11, 1)
# run_command(command_12, 1)
# run_command(command_13, 1)
# run_command(command_14, 1)
# run_command(command_15, 1)
# run_command(command_16, 1)
# run_command(command_17, 1)

# run_command(command_18, 1)
# run_command(command_19, 1)
# run_command(command_20, 1)
# run_command(command_21, 1)
# run_command(command_22, 1)
# run_command(command_23, 1)
# run_command(command_24, 1)
# run_command(command_25, 1)
# run_command(command_26, 1)
#
run_command(command_27, 1)
run_command(command_28, 1)
run_command(command_29, 1)
run_command(command_30, 1)
run_command(command_31, 1)
run_command(command_32, 1)
run_command(command_33, 1)
run_command(command_34, 1)
run_command(command_35, 1)

run_command(command_36, 1)
run_command(command_37, 1)
run_command(command_38, 1)
run_command(command_39, 1)
run_command(command_40, 1)
run_command(command_41, 1)
run_command(command_42, 1)
run_command(command_43, 1)
#
# run_command(command_44, 1)
# run_command(command_45, 1)
# run_command(command_46, 1)
# run_command(command_47, 1)
# run_command(command_48, 1)
# run_command(command_49, 1)
# run_command(command_50, 1)
# run_command(command_51, 1)