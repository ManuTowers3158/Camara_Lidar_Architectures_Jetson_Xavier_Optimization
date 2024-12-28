
# Master's Thesis: BEVFusion Optimization on Jetson Xavier

Welcome to the repository for my master's thesis. This work focuses on integrating and optimizing the BEVFusion framework on the NVIDIA Jetson Xavier platform to explore real-time performance improvements in camera-LiDAR object detection systems.

## Table of Contents

- [Abstract](#abstract)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Experiments](#experiments)
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Abstract

This thesis investigates methods to optimize the BEVFusion framework for deployment on the Jetson Xavier platform. The research explores optimization strategies to enhance performance  including: 
1. Model quantization
2. Image backbone optimization
3. Adjustments to input resolution

Performance is assessed using a comprehensive evaluation framework that considers accuracy (measured as mean Average Precision, mAP) on the NuScenes dataset, inference
 latency, power consumption, memory footprint, and robustness under adverse weather conditions. The goal is to optimize the trade-offs between these factors, ensuring that the model
 remains both effective and efficient under the limitations imposed by practical deployment scenarios.
 Results demonstrate significant improvements in runtime efficiency and energy usage while maintaining competitive accuracy, showcasing the feasibility of deploying BEV detection frameworks in constrained edge environments. 

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
- CUDA 11.4
- Python 3.8
- GCC 9.4
- CuDNN 8.6
- PyTorch 1.11.0 (Jetson Wheel)
- Torchvision (from source)
- MMCV 2.1.0 (mim install)
- MMDet >=3.0.0 (mim install)
- MMDetection3D (from source)
- CUMM (from source)
- Spconv(from source)
- NuScenes dataset (~600GB)
- Nuscenes devkit

## Installation

1. Clone mmdetection3D Repository
:
   ```bash
   git clone https://github.com/open-mmlab/mmdetection3d.git -b dev-1.x
   
   ```

2. Install pytorch wheel from [Pytorch for Jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048).

3. Download and set up the NuScenes dataset as per [NuScenes instructions](https://www.nuscenes.org).

4. Compile and install MMCV and MMDetection3D:
   ```bash
   ./scripts/install_mmdetection3d.sh
   ```
7. Install dependencies:
   ```bash
   pip install -r requirements.txt
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


