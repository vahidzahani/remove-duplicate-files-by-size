
# Remove Duplicate Files by Size

This Python script searches for duplicate files based on file size within a specified folder and its subfolders. It retains only one copy of each file with the same size and deletes the rest.

## Features
- **Scan Directories and Subdirectories**: The script recursively searches the target folder and its subfolders for all files.
- **Group Files by Size**: It categorizes files based on their size using Python’s `os` module.
- **Delete Duplicate Files**: For files with the same size, only one is kept while all others are deleted to free up space.
- **Progress Updates**: While scanning folders and deleting files, the script prints progress messages to the console.

## How It Works
1. **Folder Scanning**: The script uses the `os.walk` function to traverse the specified directory (and all its subdirectories) to find files.
   
2. **Categorizing by File Size**: For each file, the script calculates its size using the `os.path.getsize` function and groups files with the same size together.

3. **Removing Duplicates**: Once files are categorized by size, the script checks if multiple files have the same size. It then keeps only the first file in each group and deletes all others.

4. **Output**: The script outputs messages indicating which folder is being scanned and which files are being deleted.

## Usage

### Prerequisites
- Python 3.x installed on your machine.
- Basic understanding of running Python scripts.

### Instructions
1. Clone the repository or download the script.
   
   ```bash
   git clone https://github.com/yourusername/remove-duplicate-files-by-size.git
   cd remove-duplicate-files-by-size
   ```

2. Edit the `folder_path` in the script to point to the folder you want to scan. By default, it is set to a folder named `telegram`:

   ```python
   folder_path = 'telegram'
   ```

3. Run the script:

   ```bash
   python remove_duplicates.py
   ```

4. The script will scan the folder and its subdirectories, group files by size, and delete duplicates. It will output the files it deletes as it progresses.

## Example

```python
import os

folder_path = 'telegram'
files_by_size = {}

# Walk through all files in the folder and its subfolders
for root, dirs, files in os.walk(folder_path):
    print(f"Scanning folder: {root}")
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        
        # Group files by their size
        if file_size in files_by_size:
            files_by_size[file_size].append(file_path)
        else:
            files_by_size[file_size] = [file_path]

# Remove duplicate files by size
for size, files in files_by_size.items():
    if len(files) > 1:
        # Keep only the first file and delete the rest
        for file in files[1:]:
            os.remove(file)
            print(f'File {file} deleted.')

print('Duplicate files by size removed.')
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues and pull requests for improvements and bug fixes.

---

You can save this content in a file named `README.md` for your GitHub repository.

### Key Sections:
1. **Project Title**: A concise title for your script.
2. **Description**: Explanation of what the script does.
3. **Features**: Highlight important functionalities of the script.
4. **How It Works**: Breakdown of the code's logic in simple terms.
5. **Usage**: Steps to set up and run the script, including code snippets.
6. **Example**: Code sample to demonstrate usage.
7. **License**: Information about the project's licensing.
8. **Contributing**: Invitation to contribute to the project with guidelines.
