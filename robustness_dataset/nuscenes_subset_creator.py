import os
import json
import shutil
from nuscenes.nuscenes import NuScenes


def filter_and_collect_metadata(nusc, subset_dir, rain_scene_tokens):
    """
    Filters metadata for rain scenes, collects JSON files for all metadata tables,
    and saves relevant entries to the subset directory.

    Args:
        nusc (NuScenes): NuScenes dataset object.
        subset_dir (str): Directory where the subset metadata and files will be saved.
        rain_scene_tokens (list): List of scene tokens for rain scenes.
    """
    # Metadata containers for JSON outputs
    collected_scenes = []
    collected_samples = []
    collected_sample_data = []
    collected_ego_pose = []
    collected_sample_annotation = []
    timestamps = set()  # To store unique timestamps for sweep files

    # Ensure output metadata is within `v1.0-trainval`
    metadata_dir = os.path.join(subset_dir, 'v1.0-trainval')
    os.makedirs(metadata_dir, exist_ok=True)

    # Files to process
    additional_files = [
        "attribute.json",
        "calibrated_sensor.json",
        "category.json",
        "instance.json",
        "log.json",
        "map.json",
        "sensor.json",
        "visibility.json"
    ]

    # Initialize collection for additional metadata
    additional_metadata = {file: [] for file in additional_files}

    # Map to store sample_token -> list of tokens from sample_data.json and sample_annotation.json
    sample_data_map = {}
    sample_annotation_map = {}

    # Load the original JSON files
    scene_path = os.path.join(nusc.dataroot, "v1.0-trainval", "scene.json")
    sample_data_path = os.path.join(nusc.dataroot, "v1.0-trainval", "sample_data.json")
    ego_pose_path = os.path.join(nusc.dataroot, "v1.0-trainval", "ego_pose.json")
    sample_annotation_path = os.path.join(nusc.dataroot, "v1.0-trainval", "sample_annotation.json")

    with open(scene_path, 'r') as f:
        all_scenes = json.load(f)

    with open(sample_data_path, 'r') as f:
        sample_data_entries = json.load(f)

    with open(ego_pose_path, 'r') as f:
        ego_pose_entries = json.load(f)

    with open(sample_annotation_path, 'r') as f:
        sample_annotation_entries = json.load(f)

    # Load additional files
    for file in additional_files:
        file_path = os.path.join(nusc.dataroot, "v1.0-trainval", file)
        with open(file_path, 'r') as f:
            additional_metadata[file] = json.load(f)

    # Build lookup maps
    ego_pose_map = {entry["token"]: entry for entry in ego_pose_entries}
    for entry in sample_data_entries:
        sample_token = entry["sample_token"]
        if sample_token not in sample_data_map:
            sample_data_map[sample_token] = []
        sample_data_map[sample_token].append(entry)

    for entry in sample_annotation_entries:
        sample_token = entry["sample_token"]
        if sample_token not in sample_annotation_map:
            sample_annotation_map[sample_token] = []
        sample_annotation_map[sample_token].append(entry)

    for scene in all_scenes:
        if scene["token"] in rain_scene_tokens:
            collected_scenes.append(scene)
            print(f"Processing scene token: {scene['token']} ({scene['description']})")

            # Traverse all samples in the scene
            sample_token = scene['first_sample_token']
            while sample_token:
                # Get the sample metadata
                sample = nusc.get('sample', sample_token)

                # Collect the required sample metadata
                collected_samples.append({
                    "token": sample['token'],
                    "timestamp": sample['timestamp'],
                    "prev": sample['prev'],
                    "next": sample['next'],
                    "scene_token": sample['scene_token']
                })

                # Collect all related sample_data entries
                if sample_token in sample_data_map:
                    for entry in sample_data_map[sample_token]:
                        collected_sample_data.append(entry)

                        # Extract timestamp for sweep files
                        filename = os.path.basename(entry['filename'])
                        timestamp = "__".join(filename.split("__")[:-1])  # Extract timestamp
                        timestamps.add(timestamp)

                        # Copy sample files
                        src = os.path.join(nusc.dataroot, entry['filename'])
                        dst = os.path.join(subset_dir, entry['filename'])
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy(src, dst)

                        # Look up and collect the corresponding ego_pose entry
                        ego_pose_token = entry["ego_pose_token"]
                        if ego_pose_token in ego_pose_map:
                            collected_ego_pose.append(ego_pose_map[ego_pose_token])

                # Collect all related sample_annotation entries
                if sample_token in sample_annotation_map:
                    collected_sample_annotation.extend(sample_annotation_map[sample_token])

                # Move to the next sample in the scene
                sample_token = sample['next']

    # Save the collected `scene.json` metadata
    scene_json_path = os.path.join(metadata_dir, 'scene.json')
    with open(scene_json_path, 'w') as f:
        json.dump(collected_scenes, f, indent=4)

    # Save the collected `sample.json` metadata
    sample_json_path = os.path.join(metadata_dir, 'sample.json')
    with open(sample_json_path, 'w') as f:
        json.dump(collected_samples, f, indent=4)

    # Save the collected `sample_data.json` metadata
    sample_data_json_path = os.path.join(metadata_dir, 'sample_data.json')
    with open(sample_data_json_path, 'w') as f:
        json.dump(collected_sample_data, f, indent=4)

    # Save the collected `ego_pose.json` metadata
    ego_pose_json_path = os.path.join(metadata_dir, 'ego_pose.json')
    with open(ego_pose_json_path, 'w') as f:
        json.dump(collected_ego_pose, f, indent=4)

    # Save the collected `sample_annotation.json` metadata
    sample_annotation_json_path = os.path.join(metadata_dir, 'sample_annotation.json')
    with open(sample_annotation_json_path, 'w') as f:
        json.dump(collected_sample_annotation, f, indent=4)

    # Save the additional metadata files as they are
    for file, entries in additional_metadata.items():
        file_path = os.path.join(metadata_dir, file)
        with open(file_path, 'w') as f:
            json.dump(entries, f, indent=4)

    # Copy sweeps based on timestamps
    copy_sweeps_based_on_timestamps(nusc.dataroot, subset_dir, timestamps)

    # Print the number of entries in the generated files
    print(f"Number of entries in the generated scene.json file: {len(collected_scenes)}")
    print(f"Number of entries in the generated sample.json file: {len(collected_samples)}")
    print(f"Number of entries in the generated sample_data.json file: {len(collected_sample_data)}")
    print(f"Number of entries in the generated ego_pose.json file: {len(collected_ego_pose)}")
    print(f"Number of entries in the generated sample_annotation.json file: {len(collected_sample_annotation)}")
    for file in additional_files:
        print(f"Number of entries in the generated {file}: {len(additional_metadata[file])}")


def copy_sweeps_based_on_timestamps(dataroot, subset_dir, timestamps):
    """
    Searches the sweeps folder for files matching the timestamps and copies them,
    maintaining the original folder structure.

    Args:
        dataroot (str): Root directory of the original dataset.
        subset_dir (str): Directory for saving the subset.
        timestamps (set): Set of unique timestamps to match against sweep files.
    """
    sweeps_src_dir = os.path.join(dataroot, "sweeps")
    sweeps_dst_dir = os.path.join(subset_dir, "sweeps")
    os.makedirs(sweeps_dst_dir, exist_ok=True)

    for root, dirs, files in os.walk(sweeps_src_dir):
        for file in files:
            for timestamp in timestamps:
                if timestamp in file:  # Match file with timestamp
                    # Determine the relative path to maintain folder structure
                    relative_path = os.path.relpath(root, sweeps_src_dir)
                    dst_folder = os.path.join(sweeps_dst_dir, relative_path)

                    # Create destination folder if it doesn't exist
                    os.makedirs(dst_folder, exist_ok=True)

                    # Copy the sweep file
                    src = os.path.join(root, file)
                    dst = os.path.join(dst_folder, file)
                    shutil.copy(src, dst)
                    break  # Avoid duplicate copies if timestamp matches multiple files


def main():
    # Load the NuScenes dataset
    nusc = NuScenes(version='v1.0-trainval', dataroot='/media/xavier02/Sparkles1/nuscenes', verbose=True)

    # Output directory for the subset
    subset_dir = '/media/xavier02/Sparkles1/nuscenes_robustness'
    os.makedirs(subset_dir, exist_ok=True)

    # Filter for rain scenes
    rain_scene_tokens = []
    for scene in nusc.scene:
        if 'rain' in scene['description'].lower():
            rain_scene_tokens.append(scene['token'])

    print(f"Found {len(rain_scene_tokens)} rain scenes.")

    # # Limit to 10 scenes
    # limited_rain_scene_tokens = rain_scene_tokens[:2]
    # print(f"Processing {len(limited_rain_scene_tokens)} rain scenes.")

    # Collect metadata and copy files for the rain scenes
    filter_and_collect_metadata(nusc, subset_dir, rain_scene_tokens)


if __name__ == "__main__":
    main()
