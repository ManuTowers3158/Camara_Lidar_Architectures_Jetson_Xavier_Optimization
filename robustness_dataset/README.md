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

### 4. PKL files creation

Follow mm3detection guide, prior exectuing create_data, modify splits.py with the obtained by running:
 
```bash
scene_number_extraction.py
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
