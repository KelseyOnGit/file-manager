import os
import shutil
# Imports the os module, which provides a way to use operating system-dependent functionality like reading or writing to the file system.

# Imports the shutil module, which offers a number of high-level operations on files and collections of files, such as copying and moving files.

# Define the file types and corresponding folders
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar'],
}

# Create the target directories if they do not exist
def create_dirs(base_path):
    for folder in file_types.keys():#Loops through each folder name in keys of file_types (e.g., "Images", "Documents").
        dir_path = os.path.join(base_path, folder) #Creates a full path for the target folder by joining the base path with the folder name.
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)#If the directory does not exist, it creates the directory using `os.makedirs` and prints a confirmation message.
            print(f"Created directory: {dir_path}")

# Move files to the corresponding directories
def sort_files(base_path):
    for filename in os.listdir(base_path):
        file_ext = os.path.splitext(filename)[1].lower()
        file_path = os.path.join(base_path, filename)

        if os.path.isfile(file_path):  # Check if it is a file
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(base_path, folder, filename))
                    print(f"Moved: {filename} to {folder}")
                    break

# Main function
def main():
    # Specify the base directory where you want to organize files
    base_path = input("Enter the path to the directory to organize: ")

    if not os.path.exists(base_path):
        print("The specified directory does not exist.")
        return

    create_dirs(base_path)  # Create directories
    sort_files(base_path)    # Sort files

if __name__ == '__main__':
    main()

