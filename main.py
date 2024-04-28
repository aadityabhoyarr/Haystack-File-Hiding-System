import os
import time
from concurrent.futures import ThreadPoolExecutor

def create_folders_batch(folder_paths):
    for folder_path in folder_paths:
        os.makedirs(folder_path, exist_ok=True)
        print("Created folder:", folder_path)

def create_folders_parallel(root_folder, desired_nesting_level, folders, num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        level_folders = [root_folder]
        for level in range(desired_nesting_level):
            next_level_folders = [os.path.join(folder, subfolder) for folder in level_folders for subfolder in folders]
            # Batch folder creation operations to minimize disk I/O
            batch_size = min(len(next_level_folders), num_threads * 2)
            for i in range(0, len(next_level_folders), batch_size):
                batch = next_level_folders[i:i+batch_size]
                executor.submit(create_folders_batch, batch)
            level_folders = next_level_folders

if __name__ == "__main__":
    root_folder = "Folders4"
    os.makedirs(root_folder, exist_ok=True)
    print("Created root folder:", root_folder)
    
    desired_nesting_level = 5
    folders = [str(num) for num in range(10)]

# Nesting Level
# levels 3: generate 1110 folders takes  0.74 seconds
# levels 4: generate 11110 folders takes 2.42 seconds
# levels 5: generate 111110 folders takes 67.62 seconds
# levels 6: generate 1111110 folders takes 1002.05 seconds
# levels 7: generate 11111110 folders takes 14858.69 seconds (approximately 4.13 hours)
# levels 8: generate 111111110 folders takes 220269.65 seconds (approximately 61.19 hours)
# levels 9: generate 1111111110 folders takes 3264108.39 seconds (approximately 904.47 hours or 37.69 days)
#levels 10: generate 11111111110 folders takes 48406512.56 seconds (approximately 13446.25 hours or 560.26 days)

    num_threads = 205  # Adjusted concurrency level
    
    start_time = time.time()
    create_folders_parallel(root_folder, desired_nesting_level, folders, num_threads)
    end_time = time.time()
    
    print("Time taken:", end_time - start_time, "seconds")