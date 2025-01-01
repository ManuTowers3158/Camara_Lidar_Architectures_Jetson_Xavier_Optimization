# Nuscenes Robustness Dataset 

This repository contains tools and datasets tailored for evaluating the robustness of camera-LiDAR architectures. The focus is on creating and analyzing subsets of the NuScenes dataset under specific weather conditions (e.g., rain, fog) and other robustness-related scenarios.

## Features

- **Filtered NuScenes Dataset**: Tools to create subsets of NuScenes with challenging conditions like rain and fog.
- **Optimization-ready**: Designed for robust performance evaluation on resource-constrained devices like the Jetson Xavier.
- **Extensible Scripts**: Python scripts to streamline dataset preparation and filtering processes.
- **Focus on Robustness**: Enables testing and validation of camera-LiDAR fusion models under diverse scenarios.


```

## Usage

### 1. Filtering the Dataset

Run the script to filter scenes from the NuScenes dataset containing specific weather conditions:

```bash
python filter_nuscenes.py --condition rain --output_dir ./filtered_data
```

### 2. Data Analysis

Once the filtered dataset is created, use the analysis tools to generate insights about the selected subsets:

```bash
python analyze_data.py --input_dir ./filtered_data
```

### 3. Integration with BEVFusion

The filtered datasets are designed to integrate seamlessly with BEVFusion for performance evaluation and optimization.

## File Structure

```
robustness_dataset/
├── nuscenes_weather_filter.py       #Scan Nuscenes that fit a weather description.  
├── scene_number_extraction.py       #Suportive script that provide an list with al scenes number from a filtered search.
├── nuscenes_subset_creator.txt      #Script that creates a Nuscenes subset that satisfy a desired weather condition.  
├── validate_nuscenes_metadata.txt   #Script that validate the metadata in the subset created is valid.
└── README.md             
```
