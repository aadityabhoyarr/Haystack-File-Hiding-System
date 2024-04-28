# Haystack File Hiding System (HFHS)
####  HFHS (Haystack File Hiding System) is designed to protect your important files by hiding them within a complex maze of folders. Just like finding a needle in a haystack, locating these files without knowing the exact pattern used for folder creation is near impossible. Keep your files safe and secure with HFHS!"

## How it can be used

HFHS provides two scripts:
1.  **main.py**: This script generates a complex folder structure, making it difficult to locate specific files without prior knowledge of the pattern used for folder creation.
2.  **del.py**: This script deletes the folders and files created by the `main.py` script in a fast and efficient manner.


## How to Use

To use HFHS:

1.  Clone the repository to your local machine.
2.  Navigate to the repository directory.
3.  Open `main.py` in a text editor.
4.  Adjust the `desired_nesting_level` and `num_threads` variables according to your needs:
    -   **desired_nesting_level**: This variable determines how deep the folder structure will be. Higher values result in more complex folder structures with more levels of nesting. Lower values create simpler structures. Adjust this value based on how hidden you want your files to be within the folder maze. For example, setting `desired_nesting_level = 5` will create a moderately complex folder structure.
    -   **num_threads**: This variable controls the concurrency level, i.e., the number of threads used for parallel execution of folder creation operations. Increasing this value may speed up the folder creation process, but it depends on your system's capabilities. Be cautious not to set it too high, as it may overload your system. For example, setting `num_threads = 205` will utilize 205 threads for parallel execution.
5.  Save the changes to `main.py`.
6.  Run `main.py` to generate the folder structure.
7.  Run `del.py` to delete the created folders and files.

## About Nesting Level

The time taken to generate folder structures at different nesting levels may vary based on your computer's CPU specifications. The following information is based on a developer PC with a CPU containing `4 threads` and `4 cores`:

| Nesting Level | Number of Folders | Time Taken          |
|---------------|-------------------|---------------------|
| Level 3       | 1110              | 0.74 seconds        |
| Level 4       | 11110             | 2.42 seconds        |
| Level 5       | 111110            | 67.62 seconds       |
| Level 6       | 1111110           | 1002.05 seconds     |
| Level 7       | 11111110          | Approximately 4.13 hours |
| Level 8       | 111111110         | Approximately 61.19 hours |
| Level 9       | 1111111110        | Approximately 904.47 hours or 37.69 days |
| Level 10      | 11111111110       | Approximately 13446.25 hours or 560.26 days |

## Folder Structure Graph Representation

Here's a graphical representation of the folder structure created by HFHS at nesting level 3:

## Force-directed graph drawing of 1110

Here's a force-directed graph drawing of the folder structure created by HFHS at nesting level 3:

