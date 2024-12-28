import os
import subprocess
import time
import traceback

import spconv
print(spconv.__version__)
import schedule, time ,os
import smtplib
import random


# Define the commands for different tests
#Initial default mode 4, swin, own checkpoint in fp 32
command_1 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-cyclic-20e_nus-3d.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Camara_lidar_swin_fp32.pth"
##Initial swin, own checkpoint in fp 32 max power
command_2 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-cyclic-20e_nus-3d.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Camara_lidar_swin_fp32.pth"
##Initial swin, own checkpoint in fp 32 max power sponv
command_3 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-cyclic-20e_nus-3d.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Camara_lidar_swin_fp32.pth"
##Initial swin, own checkpoint in max power sponv checpoint fp16
command_4 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-cyclic-20e_nus-3d.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"

##Initial swin, own checkpoint  max power sponv checpoint fp16 AUTOCAST
command_5 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-cyclic-20e_nus-3d.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
#***** STARTING HERE ALL CONFIGS ARE MAX POWER SPCONV CHECKPOINT FP16 AUTOCAST
#Resnet 50
command_6 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_with_resnet_50.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
#Resnet 34
command_7 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_with_resnet_34.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
#Resnet 18
command_8 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_with_resnet_18.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
#****Using resnet 18 checkpoint
#Resnet 50
command_9 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_with_resnet_50.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_Lidar_wResnet18_checkpoint.pth"
#Resnet 34
command_10 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_with_resnet_34.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_Lidar_wResnet18_checkpoint.pth"
#Resnet 18
command_11 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_with_resnet_18.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_Lidar_wResnet18_checkpoint.pth"

#Resnet 18 +4 sweeps
command_14 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_4s_resnet18.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
#Resnet 18 +1 sweeps
command_15 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_1s_resnet18.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
#Resnet 18 + 50% resolution
command_16 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_125k_resnet18.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"
#Resnet 18 + 25% resolution
command_17 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar-cam_voxel0075_62k_resnet18.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth"




##Lidar testing
# Sequence 1: Test lidar sweeps
command_100 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_9sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_101 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_8sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_102 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_7sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_103 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_6sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_104 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_5sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_105 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_4sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_106 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_3sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_107 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_2sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_108 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_1sweeps.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"

# Sequence 1.5: Test lidar sweeps w checkpoint in 4sweeps
command_110 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_9sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_111 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_8sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_112 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_7sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_113 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_6sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_114 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_5sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_115 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_4sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_116 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_3sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_117 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_2sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"
command_118 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_1sweeps.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0075_4sweeps.pth"

# Sequence 2: Test lidar points resolution
command_120 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_225k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_121 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_200k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_122 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_175k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_123 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_150k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_124 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_125k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_125 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_100k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_126 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_75k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"
command_127 = "python tools/test.py projects/BEVFusion/configs/LIdar_resolution_configs/bevfusion_lidar_voxel0075_62k.py projects/BEVFusion/configs/MMCV_Lidar_own.pth"

#Sequence 3: Test voxel 2x
command_130 = "python tools/test.py projects/BEVFusion/configs/bevfusion_lidar_voxel0150_second_secfpn.py projects/BEVFusion/configs/Lidar_checkpoint_voxel_0150.pth"


# Function to extract the correct configuration name from the command
def extract_config_name(command):
    parts = command.split()
    for part in parts:
        # Identify the config file as any .py file in the configs directory
        if "configs/" in part and part.endswith(".py"):
            config_name = os.path.basename(part).replace(".py", "")
            return config_name
    return "default_config"
#
# # Function to run a command N times with dynamic tegrastats logging
def run_command(command, times):
    config_name = extract_config_name(command)  # Get the config name from the command

    for run_count in range(1, times + 1):
        # Create a unique log file name using the run counter
        log_file_name = f"tegrastats_{config_name}_run{run_count}.txt"

        # Automatically input the sudo password for tegrastats
        password = "xavier"  # Set your sudo password here
        tegrastats_command = f"echo {password} | sudo -S /usr/bin/tegrastats --interval 1000"

        # Start Jetson tegrastats with sudo, logging to a configuration-specific file
        tegrastats_process = subprocess.Popen(
            tegrastats_command,
            stdout=open(log_file_name, "w"),
            stderr=subprocess.STDOUT,
            shell=True
        )

        # Small delay to ensure tegrastats has started
        time.sleep(2)

        try:
            print(f"Running iteration {run_count} of command: {command}")
            os.system(command)

        finally:
            # Terminate tegrastats after this command completes
            subprocess.run("sudo pkill tegrastats", shell=True)
            time.sleep(1)  # Ensure tegrastats stops fully
            print(f"Terminated tegrastats for configuration: {config_name}, iteration: {run_count}")


# Function to run a command N times without tegrastats logging
# def run_command(command, times):
#     config_name = extract_config_name(command)  # Get the config name from the command
#
#     for run_count in range(1, times + 1):
#         # Create a unique log file name using the run counter
#         log_file_name = f"log_{config_name}_run{run_count}.txt"
#
#         try:
#             print(f"Running iteration {run_count} of command: {command}")
#             os.system(command)
#             print(f"Completed iteration {run_count} for configuration: {config_name}")
#         except:
#             traceback.print_exc()
#
#         #finally:
#             #sendMail(command, times)


# Run each scheme separately to generate individual tegrastats logs
#run_command(command_3, 3) #Example Run scheme 3, 3 times
#run_command(command_2, 3)
#run_command(command_4, 1)


run_command(command_5, 3)
