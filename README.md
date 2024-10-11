# Haystack File Hiding System (HFHS)

## Overview
HFHS (Haystack File Hiding System) is a sophisticated file protection system that creates an intricate maze of nested folders to secure files. Just as finding a needle in a haystack is nearly impossible without knowing where to look, locating files within this complex directory structure becomes extremely challenging without knowledge of the exact pattern used.

## System Components

### 1. Folder Generation Script (`main.py`)
This script generates a complex folder structure, making it difficult to locate specific files without prior knowledge of the pattern used for folder creation.

### 2. Cleanup Utility (`del.py`)
This script deletes the folders and files created by the `main.py` script in a fast and efficient manner.

## Usage Guide

### Basic Setup and Configuration

1. Open `main.py` and configure key parameters:
```python
root_folder = "Folders4"              # Base folder name
desired_nesting_level = 5             # Depth of folder structure
folders = [str(num) for num in range(10)]  # Subfolder names (0-9)
num_threads = 205                     # Number of parallel threads
```

2. Run the folder generation script:
```bash
python main.py
```

3. To remove the structure:
```bash
python del.py
```

### Folder Structure Visualization

The system creates a nested structure like this:
```
Folders4/
├── 0/
│   ├── 0/
│   │   ├── 0/
│   │   ├── 1/
│   │   └── ...
│   ├── 1/
│   │   ├── 0/
│   │   ├── 1/
│   │   └── ...
│   └── ...
├── 1/
│   ├── 0/
│   ├── 1/
│   └── ...
└── ...
```

### Performance Metrics

Execution times based on a 4-core/4-thread CPU:

| Nesting Level | Folders Created | Time Required |
|---------------|----------------|---------------|
| 3 | 1,110 | 0.74 seconds |
| 4 | 11,110 | 2.42 seconds |
| 5 | 111,110 | 67.62 seconds |
| 6 | 1,111,110 | 16.7 minutes |
| 7 | 11,111,110 | 4.13 hours |
| 8 | 111,111,110 | 2.5 days |
| 9 | 1,111,111,110 | 37.69 days |
| 10 | 11,111,111,110 | 560.26 days |

Here's a graphical representation of the folder structure created by HFHS at nesting level 3:
<img src="https://github.com/aadityabhoyar/Haystack-File-Hiding-System/blob/main/media/Figure_1.png">


## Force-directed graph drawing of 1110 Folders at level 3

<img src="https://github.com/aadityabhoyar/Haystack-File-Hiding-System/blob/main/media/Figure_2.png">

