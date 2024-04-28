import os
import time
from concurrent.futures import ThreadPoolExecutor

def delete_files_and_folders(root_folder):
    for root, dirs, files in os.walk(root_folder, topdown=False):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
                print("Deleted file:", os.path.join(root, file))
            except Exception as e:
                print("Error deleting file:", os.path.join(root, file), "-", e)
        for dir in dirs:
            try:
                os.rmdir(os.path.join(root, dir))
                print("Deleted folder:", os.path.join(root, dir))
            except Exception as e:
                print("Error deleting folder:", os.path.join(root, dir), "-", e)

def delete_files_and_folders_parallel(root_folder, num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.submit(delete_files_and_folders, root_folder)

if __name__ == "__main__":
    root_folder = "root"
    num_threads = 205  # Adjusted concurrency level
    
    start_time = time.time()
    delete_files_and_folders_parallel(root_folder, num_threads)
    end_time = time.time()
    
    print("Time taken:", end_time - start_time, "seconds")
