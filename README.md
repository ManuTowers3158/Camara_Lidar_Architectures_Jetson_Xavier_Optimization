
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
