# Nuscenes Robustness Dataset 

This repository contains tools and datasets tailored for evaluating the robustness of camera-LiDAR architectures. The focus is on creating and analyzing subsets of the NuScenes dataset under specific weather conditions (e.g., rain, fog) and other robustness-related scenarios.



## Usage

### 1. Filtering the Dataset

Run the script to filter scenes from the NuScenes dataset containing specific weather conditions: 

```bash
python nuscenes_weather_filter.py 
```


### 2. Create Robustness subset dataset

Run the script to create the robustness subset. 

```bash
python nuscenes_subset_creator.py 
```

### 3. Subset Validation

Once subset is created, run validation script to verify metadata is correct.

```bash
python validate_nuscenes_metadata.py 
```

### 4. PKL files creation for mmdetection3D

Follow [mm3detection guide](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/nuscenes.html), prior exectuing create_data.py, modify splits.py with the array list obtained by running:
 
```bash
scene_number_extraction.py
```
After modifying the splits.py file:
```bash
python tools/create_data.py nuscenes --root-path ./data/robustness_nuscenes --out-dir ./data/robustness_nuscenes --extra-tag nuscenes
```

## File Structure

```
robustness_dataset/
├── nuscenes_weather_filter.py       #Scan Nuscenes that fit a weather description.  
├── scene_number_extraction.py       #Suportive script that provide an list with al scenes number from a filtered search.
├── nuscenes_subset_creator.txt      #Script that creates a Nuscenes subset that satisfy a desired weather condition.  
├── validate_nuscenes_metadata.txt   #Script that validate the metadata in the subset created is valid.
└── README.md             
```
