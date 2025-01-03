
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

3. Clone Torchvision Repository inside mmdetection3D Repository
:
   ```bash
   git clone https://github.com/pytorch/vision.git
   ```	
4. Install Torchvision:
    ```	
	python setup.py install
    ```	

5. Install MMCV and MMDET using MIM installation as per guide[MMDetection 3D](https://mmdetection3d.readthedocs.io/en/latest/get_started.html)
6. Instal from source MMDetection 3D:
    ```bash
   	cd mmdetection3d
	pip install -v -e .
    ```	
   Note: During mmdetection3d installation user may need to manually hardcode and override the minimum mmcv version to the version that was installed from source.

7. Clone cumm and spconv repositories inside mmdetection 3D repository.
    ```bash
    git clone https://github.com/FindDefinition/cumm.git
    git clone https://github.com/traveller59/spconv.git
    ```	
8. Install cumm from source as per guide in [cumm repository](https://github.com/FindDefinition/cumm?tab=readme-ov-file). 
9. Install spconv from source as per guide in [spconv repository](https://github.com/traveller59/spconv).

   Note: during spconv installation prior executing "pip install -e" make sure you run and verify spconv is operating:
    ```bash
	export PYTHONPATH=$PYTHONPATH:/$userpath/mmdetection3d-main/cumm
	export PYTHONPATH=$PYTHONPATH:/$userpath/mmdetection3d-main/spconv
	export CUMM_CUDA_ARCH_LIST="7.2"
	python3
	import spconv
	print(spconv.__version__)
	exit()
    ```	




10. Download and set up the NuScenes dataset as per [NuScenes instructions](https://www.nuscenes.org). Recommended to have 1TB External SSD.

## Usage

Copy config files inside projects/BEVFusion/configs

Copy test scripts inside mmdetection3d/tools/

Copy bevfusion_necks.py inside mmdetection3d/projects/BEVFusion/bevfusion

For schemes 4-17 and lidar experiments, replace original bevfusion.py with bevfusion.py from this repo. 

### Running Inference and tegrastats logging
To run inference on multiple schemes from scheme 4 to 17 in automated sequence use:

	python tools/Test_Automation.py

To run inference on a single scheme, inside Test_Automation.py use one of the availables command lines, example:


	python tools/test.py projects/BEVFusion/configs/bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-	cyclic-20e_nus-3d.py /media/xavier02/xavier_ssd_500/mmdetection3d_source/mmdetection3d-	main/projects/BEVFusion/configs/Cam_lid_ep6_fp16.pth
    

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

The expirments are divided as follow:

Initial Baseline: 
	Scheme 1 | Jetson Xavier configured in default mode
HW/SW Max Performance:
	Scheme 2 | Jetson Xavier configured to MAX performance mode
	Scheme 3 | Scheme 2 + Spconv libray 
Model Quantization:
	Scheme 4 | Scheme 3 + Model weights in FP16
	Scheme 5 | Scheme 4 + Use of torch.autocast() function
Image Backbone Optimization:
	Scheme 6 | Scheme 5 / Resnet 50 as image backbone
	Scheme 7 | Scheme 5 / Resnet 34 as image backbone
	Scheme 8 | Scheme 5 / Resnet 18 as image backbone
	Scheme 9 | Scheme 8 / model retrained with Resnet 18
	Scheme 10| Scheme 5/ image tensor set to zero prior to sensor fusion
Input Size Resolution:
	Scheme 11|Scheme 5 /LiDAR input using only 4 sweeps 
	Scheme 12|Scheme 5 /LiDAR input using only 1 sweep 
	Scheme 13|Scheme 5 /LiDAR input using 50% point cloud 
	Scheme 14|Scheme 5 /LiDAR input using 25% point cloud 

## Results Table

The table below summarizes the performance metrics for various schemes:

| Scheme    | Accuracy | Latency (ms) | Robustness | Average Power (mW) | Energy per Inference (J) | Average RAM (MB) | RAM Needed by Inference (MB) |
|-----------|----------|--------------|------------|---------------------|--------------------------|------------------|------------------------------|
| Scheme 1  | 0.6494   | 2573         | 0.641      | 9227.81            | 23.743                  | 12733.66         | 32763.707                   |
| Scheme 2  | 0.6494   | 1850         | 0.641      | 20763              | 38.412                  | 12521            | 23163.850                   |
| Scheme 3  | 0.6497   | 1745         | 0.641      | 19059              | 33.258                  | 15318            | 26729.910                   |
| Scheme 4  | 0.6523   | 1710         | 0.640      | 16554.63           | 31.715                  | 15214            | 26015.940                   |
| Scheme 5  | 0.6514   | 1447         | 0.640      | 16554.63           | 23.955                  | 15603.00         | 22577.541                   |
| Scheme 6  | 0.605    | 1278         | 0.638      | 15310.64           | 19.567                  | 14859.83         | 18990.863                   |
| Scheme 7  | 0.6507   | 1270         | 0.640      | 15731.7            | 19.979                  | 14357.00         | 18233.390                   |
| Scheme 8  | 0.6507   | 1247         | 0.637      | 15219              | 18.978                  | 14143.00         | 17636.321                   |
| Scheme 9  | 0.6298   | 890          | 0.6135     | 15219              | 18.978                  | 13710            | 12201.900                   |
| Scheme 14 | 0.626    | 814          | 0.617      | 14468.11           | 11.777                  | 13525.77         | 11009.977                   |
| Scheme 15 | 0.560    | 668          | 0.5317     | 14012              | 9.360                   | 13247.45         | 8849.297                    |
| Scheme 16 | 0.607    | 830          | 0.600      | 14523.23           | 12.054                  | 13909.42         | 11544.819                   |
| Scheme 17 | 0.520    | 703          | 0.517      | 14294.69           | 10.049                  | 13156.76         | 9249.202                    |




### Key Observations
- **ResNet-18** achieves a good balance between speed and accuracy.
- **ResNet-50** offers higher accuracy at the cost of increased latency and memory usage.
- **MobileNetV2** is the fastest but sacrifices some accuracy.


## Contributing

Contributions, issues, and feature requests are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md).

## Acknowledgments

Special thanks to my thesis advisor, lab colleagues, and the developers of the BEVFusion framework. This research was made possible by resources provided by [NVIDIA](https://www.nvidia.com) and the open-source NuScenes dataset.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

=======


