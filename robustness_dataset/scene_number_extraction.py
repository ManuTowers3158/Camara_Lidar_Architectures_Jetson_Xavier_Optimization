# Read the content of the text file
with open('/media/xavier02/Sparkles1/nuscenes_robustness/rain_scenes.txt', 'r') as file:  # Replace 'scenes.txt' with the actual file name
    lines = file.readlines()

# Extract scene numbers
scene_numbers = []
for line in lines:
    if line.startswith("scene-"):
        scene_numbers.append(line.strip())

# Format the list as desired
formatted_list = f"val = \\\n    {scene_numbers}"

# Print the result
print(formatted_list)

# Optional: Save to a file
with open('output.txt', 'w') as output_file:
    output_file.write(formatted_list)
