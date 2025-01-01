# Robustness Dataset for Camera-LiDAR Architectures Optimization

This repository contains tools and datasets tailored for evaluating the robustness of camera-LiDAR architectures optimized for Jetson Xavier. The focus is on creating and analyzing subsets of the NuScenes dataset under specific weather conditions (e.g., rain, fog) and other robustness-related scenarios.

## Features

- **Filtered NuScenes Dataset**: Tools to create subsets of NuScenes with challenging conditions like rain and fog.
- **Optimization-ready**: Designed for robust performance evaluation on resource-constrained devices like the Jetson Xavier.
- **Extensible Scripts**: Python scripts to streamline dataset preparation and filtering processes.
- **Focus on Robustness**: Enables testing and validation of camera-LiDAR fusion models under diverse scenarios.

## Requirements

Before using this repository, ensure you have the following installed:

- Python 3.8+
- Required Python libraries (listed in `requirements.txt`).
- Access to the NuScenes dataset (full dataset required).

To install dependencies:

```bash
pip install -r requirements.txt
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
├── filter_nuscenes.py    # Script to filter the NuScenes dataset
├── analyze_data.py       # Tools for analyzing the filtered dataset
├── requirements.txt      # Required Python dependencies
└── README.md             # Project documentation
```

## Future Work

- Add support for additional weather conditions (e.g., snow, haze).
- Include benchmarking tools for model evaluation.
- Optimize filtering and analysis processes for speed and scalability.

## Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, feel free to reach out:

- **Author**: Manuel Torres  
- **Email**: [YourEmail@example.com]  
- **GitHub**: [ManuTowers3158](https://github.com/ManuTowers3158)
