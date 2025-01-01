def process_memory_usage(file_path):
    # Initialize lists to store memory values
    backbone_memory = []
    neck_memory = []

    # Conversion factor: 1 MB = 1,048,576 bytes
    BYTES_TO_MB = 1_048_576

    # Open and read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Parse memory usage for camera backbone
            if line.startswith("Memory used by camera backbone:"):
                value = int(line.split(":")[1].strip().split()[0])
                backbone_memory.append(value / BYTES_TO_MB)
            # Parse memory usage for camera neck
            elif line.startswith("Memory used by camera neck:"):
                value = int(line.split(":")[1].strip().split()[0])
                neck_memory.append(value / BYTES_TO_MB)

    # Calculate statistics
    avg_backbone_memory = sum(backbone_memory) / len(backbone_memory) if backbone_memory else 0
    avg_neck_memory = sum(neck_memory) / len(neck_memory) if neck_memory else 0

    # Print results
    print("Camera Backbone Memory Usage (in MB):")
    print(f"  Total Entries: {len(backbone_memory)}")
    print(f"  Average: {avg_backbone_memory:.2f} MB")
    print(f"  Values: {backbone_memory}")
    print("\nCamera Neck Memory Usage (in MB):")
    print(f"  Total Entries: {len(neck_memory)}")
    print(f"  Average: {avg_neck_memory:.2f} MB")
    print(f"  Values: {neck_memory}")



# Example usage
file_path = "Memory used by camera backbone RES18.txt"  # Replace with your file path
process_memory_usage(file_path)
