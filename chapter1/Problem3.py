import os

def list_directory_contents(path):
    try:
        # List the files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access {path}.")

# Replace 'your_directory_path' with the path of the directory you want to list
list_directory_contents('/hp')
