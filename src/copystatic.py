import os,shutil

# Recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
def recurse_copy_dir(source,destination):
    # Copy all files and subdirectories, nested files, etc.
    if os.path.exists(source):
        if os.path.isdir(source):
            children = os.listdir(source)
            # Recursion
            for child in children:
                full_path = os.path.join(source,child)
                if os.path.isdir(full_path):
                    full_des_path = os.path.join(destination,child)
                    os.mkdir(full_des_path)
                    recurse_copy_dir(full_path,full_des_path)
                    continue
                print(f"Copying {full_path} to {destination}")
                shutil.copy(full_path,destination)
        else:
            raise NotADirectoryError(f"{source} is not a directory.")
    else:
        raise FileNotFoundError(f"{source} does not exist.")
    
# Function to delete a directory and create an empty folder of the same name. 
# Used for copying files and ensuring the copy is clean.
def wipe_dir(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
    os.mkdir(path)