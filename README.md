<<<<<<< HEAD

# Master's Thesis: BEVFusion Optimization on Jetson Xavier

Welcome to the repository for my master's thesis. This work focuses on integrating and optimizing the BEVFusion framework on the NVIDIA Jetson Xavier platform to explore real-time performance improvements in camera-LiDAR object detection systems.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Experiments](#experiments)
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

This thesis investigates methods to optimize the BEVFusion framework for deployment on the Jetson Xavier platform. Key objectives include:
- Reducing inference latency through model adjustments.
- Evaluating performance trade-offs between memory usage and computational speed.
- Enhancing real-time processing capabilities for autonomous driving applications.

**Keywords**: BEVFusion, Jetson Xavier, Optimization, Real-Time Inference, Autonomous Driving

## Repository Structure

```
├── configs/                # Configuration files for training and testing
├── data/                   # NuScenes dataset and subsets
├── scripts/                # Scripts for experiments and metrics logging
├── results/                # Logs, metrics, and results of experiments
├── src/                    # Core BEVFusion framework and modifications
├── notebooks/              # Jupyter notebooks for analysis
└── README.md               # This file
```

## Requirements

- NVIDIA Jetson Xavier with JetPack 5.1.3
- Python 3.8
- PyTorch 1.11.0
- CUDA 11.4
- MMDetection3D and MMCV 2.1.0
- NuScenes dataset (~600GB)
- Additional Python dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-thesis-repo.git
   cd your-thesis-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up the NuScenes dataset as per [NuScenes instructions](https://www.nuscenes.org).

4. Compile and install MMCV and MMDetection3D:
   ```bash
   ./scripts/install_mmdetection3d.sh
   ```

## Usage

### Running Inference
To run inference on a test dataset and log system metrics:
```bash
python src/test.py --config configs/resnet18_config.py --checkpoint checkpoints/resnet18.pth
```

### Measuring Performance
Use the provided scripts in the `scripts` folder to monitor system metrics during inference:
```bash
tegrastats | python scripts/log_metrics.py
```

### Visualization
To visualize results or create 3D LiDAR visualizations:
```bash
python src/visualize_lidar.py --data-path data/nuscenes
```

## Experiments

Detailed experiments include:
1. Backbone Analysis: ResNet-18 vs. ResNet-50
2. Quantization: Float32 vs. Int8 models
3. LiDAR Sweep Reduction: Impact on memory and latency
4. FP16 Optimization: Enabling half-precision in voxelization and sparse encoder

## Results

- Achieved a **50% reduction in latency** through model adjustments and optimizations.
- Increased memory usage slightly to enable faster inference.
- Quantitative results and visualizations are stored in the `results/` folder.

## Contributing

Contributions, issues, and feature requests are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md).

## Acknowledgments

Special thanks to my thesis advisor, lab colleagues, and the developers of the BEVFusion framework. This research was made possible by resources provided by [NVIDIA](https://www.nvidia.com) and the open-source NuScenes dataset.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
=======
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
>>>>>>> 1b16c5b59fdc8af79766c9f57b3ba1d6dfb6a714
