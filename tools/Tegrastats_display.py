import re

# Load the log data from a text file
#log_file_path = "M:\\Master THI\\4th Semester\\Python Scripts\\tegrastats_log_befusion_inital_baseline.txt"
log_file_path = "C:\\Users\\Compu Manu\\Desktop\\Thesis local\\Final Logs\\Power Memory\\PM 4\\tegrastats_bevfusion_lidar-cam_voxel0075_second_secfpn_8xb4-cyclic-20e_nus-3d_run2.txt"
# Initialize cumulative variables and counters
total_ram_usage = 0
total_swap_usage = 0
total_gpu_utilization = 0
total_gpu_frequency = 0
total_cpu_power = 0
total_gpu_power = 0
total_soc_power = 0
total_energy_consumption = 0  # Sum of CPU, GPU, and SOC power
entry_count = 0

# Track consecutive non-zero GPU utilization entries
consecutive_non_zero_count = 0
start_calculation = False

# Open the file and read all lines
with open(log_file_path, 'r') as file:
    log_data = file.readlines()

# Ignore the first 20 and last 20 entries
log_data = log_data[0:-1]

# Iterate through each line (each timestamp entry)
for entry in log_data:
    # Match the RAM usage (e.g., RAM 10588/30991MB)
    ram_usage_match = re.search(r'RAM (\d+)/(\d+)MB', entry)
    # Match the SWAP usage (e.g., SWAP 0/15495MB)
    swap_usage_match = re.search(r'SWAP (\d+)/(\d+)MB', entry)
    # Match the GPU utilization and frequency (e.g., GR3D_FREQ 10%@[318])
    gpu_usage_match = re.search(r'GR3D_FREQ (\d+)%@\[(\d+)\]', entry)
    # Match CPU, GPU, and SOC power (e.g., GPU 616mW, CPU 1541mW, SOC 1387mW)
    cpu_power_match = re.search(r'CPU (\d+)mW/', entry)
    gpu_power_match = re.search(r'GPU (\d+)mW/', entry)
    soc_power_match = re.search(r'SOC (\d+)mW/', entry)

    # RAM usage extraction
    if ram_usage_match:
        ram_used = int(ram_usage_match.group(1))
        total_ram_usage += ram_used

    # SWAP usage extraction
    if swap_usage_match:
        swap_used = int(swap_usage_match.group(1))
        total_swap_usage += swap_used

    # GPU usage and frequency extraction
    if gpu_usage_match:
        gpu_percent = int(gpu_usage_match.group(1))
        gpu_frequency = int(gpu_usage_match.group(2))

        # Track consecutive non-zero entries
        if gpu_percent > 0:
            consecutive_non_zero_count += 1
        else:
            consecutive_non_zero_count = 0  # Reset if a zero entry is found

        # Start calculating only after three consecutive non-zero entries
        if consecutive_non_zero_count >= 3:
            start_calculation = True

        # Accumulate values if calculation has started
        if start_calculation:
            total_gpu_utilization += gpu_percent
            total_gpu_frequency += gpu_frequency
            entry_count += 1

    # Accumulate power readings for CPU, GPU, and SOC if calculation has started
    if start_calculation:
        if cpu_power_match:
            cpu_power = int(cpu_power_match.group(1))
            total_cpu_power += cpu_power
        if gpu_power_match:
            gpu_power = int(gpu_power_match.group(1))
            total_gpu_power += gpu_power
        if soc_power_match:
            soc_power = int(soc_power_match.group(1))
            total_soc_power += soc_power

# Calculate averages if entries were found
average_ram_usage = total_ram_usage / entry_count if entry_count > 0 else 0
average_swap_usage = total_swap_usage / entry_count if entry_count > 0 else 0
average_gpu_utilization = total_gpu_utilization / entry_count if entry_count > 0 else 0
average_gpu_frequency = total_gpu_frequency / entry_count if entry_count > 0 else 0
average_cpu_power = total_cpu_power / entry_count if entry_count > 0 else 0
average_gpu_power = total_gpu_power / entry_count if entry_count > 0 else 0
average_soc_power = total_soc_power / entry_count if entry_count > 0 else 0
total_energy_consumption = (total_cpu_power + total_gpu_power + total_soc_power) / entry_count if entry_count > 0 else 0

# Output the calculated averages
print(f"Average RAM usage: {average_ram_usage:.2f} MB")
print(f"Average SWAP usage: {average_swap_usage:.2f} MB")
print(f"Average GPU utilization: {average_gpu_utilization:.2f}%")
print(f"Average GPU frequency: {average_gpu_frequency:.2f} MHz")
print(f"Average CPU power consumption: {average_cpu_power:.2f} mW")
print(f"Average GPU power consumption: {average_gpu_power:.2f} mW")
print(f"Average SOC power consumption: {average_soc_power:.2f} mW")
print(f"Total average energy consumption: {total_energy_consumption:.2f} mW")
