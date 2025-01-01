from nuscenes.nuscenes import NuScenes

# Correct path to the dataset root folder
nusc = NuScenes(version='v1.0-trainval', dataroot='/media/xavier02/Sparkles1/nuscenes', verbose=True)

# Retrieve all scenes and their descriptions
scene_weather_info = []

for scene in nusc.scene:
    scene_name = scene['name']
    scene_description = scene['description']
    scene_weather_info.append((scene_name, scene_description, scene))

# Print weather-related information for all scenes
print("Weather-Related Information for All Scenes:")
for scene_name, description, _ in scene_weather_info:
    print(f"Scene: {scene_name}, Description: {description}")

# Filter for night scenes
night_scenes = []

for scene_name, description, scene_data in scene_weather_info:
    if 'haze' in description.lower():
        night_scenes.append(scene_data)

# Print the filtered night scenes to the console
print("\nhaze Scenes:")
for scene in night_scenes:
    print(f"Scene Name: {scene['name']}, Description: {scene['description']}")

# Print full scene information for the filtered night scenes
print("\nFiltered haze Scenes Full Information:")
for scene in night_scenes:
    print(scene)

# Write the night scenes to a text file
output_file = "/media/xavier02/Sparkles1/nuscenes_robustness/haze_scenes.txt"
with open(output_file, "w") as file:
    for scene in night_scenes:
        file.write(f"{scene['name']}\n")
        file.write(f"Full Information: {scene}\n\n")

print(f"\nHaze scenes have also been written to {output_file}.")
