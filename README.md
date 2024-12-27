# Camara_Lidar_Architectures_Jetson_Xavier_Optimization
 
Master Thesis: Optimizing BEVFusion Framework for Jetson Xavier

This repository contains the code, documentation, and results for my master thesis, which focuses on integrating and optimizing the BEVFusion framework for the Jetson Xavier platform. The objective of this work is to enhance inference performance while maintaining model accuracy, particularly for camera-LiDAR object detection tasks.

Repository Structure

configs/: Configuration files for BEVFusion experiments, including different backbones and parameter settings.

scripts/: Utility scripts for running experiments, collecting metrics, and automating tasks.

notebooks/: Jupyter notebooks for data analysis and visualization of results.

data/: Scripts and instructions for working with the NuScenes dataset.

results/: Output files, including logs, charts, and tables summarizing key findings.

docs/: Supplementary documentation for installation, usage, and methodology.

Key Features

BEVFusion Framework: Integrates and adapts the BEVFusion framework to the Jetson Xavier environment.

Backbone Customization: Experiments with various backbones (e.g., ResNet, MobileNet) to evaluate their impact on performance.

Optimization Techniques:

Precision reduction (FP16 and INT8 quantization).

Sweeps reduction and voxel size adjustments for faster processing.

Metrics Collection: Scripts for recording latency, memory usage, and power consumption using tegrastats.

Visualization: Tools for 3D visualization of LiDAR data and performance charts.

Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/master-thesis.git
cd master-thesis

Install dependencies:

Ensure that you have JetPack 5.1.3, CUDA 11.4, and PyTorch 1.11 installed.

Install required Python packages:

pip install -r requirements.txt

Prepare the NuScenes dataset:

Download the dataset from NuScenes and follow the instructions in data/README.md to set up.

How to Run

Training and Inference:

Use the provided scripts in scripts/ to run training or inference:

python scripts/train.py --config configs/resnet50.yaml
python scripts/test.py --config configs/resnet50.yaml

Metrics Collection:

Run inference while logging performance metrics:

python scripts/run_with_metrics.py --config configs/resnet50.yaml

Visualization:

Generate visualizations of LiDAR sweeps:

python scripts/visualize_lidar.py --num 100

Results Summary

Inference Performance:

Achieved a latency reduction from 2667ms to 1317ms by switching backbones and enabling precision optimizations.

Memory Usage:

Increased from 15GB to 16GB after swapping from Swin-Tiny to ResNet-18.

Power Consumption:

Data collected using tegrastats, with comprehensive analysis available in results/power_metrics.csv.

Future Work

Apply dynamic quantization to reduce model size and improve performance.

Experiment with additional backbones and optimization methods.

Extend the framework to support other datasets and platforms.

Contact

For questions or feedback, feel free to reach out:

Name: Manuel Torres

Email: manuel.torres@example.com

GitHub: ManuelTorres
