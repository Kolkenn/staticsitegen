from textnode import TextNode, TextType
import os,shutil

def main():
    recurse_copy_dir("./static","./public")

def wipe_dir(path):
    # Delete all the contents of the destination directory (public) to ensure that the copy is clean.
    if os.path.exists(path):
        if os.path.isdir(path):
            print(f"Removing {path} directory")
            shutil.rmtree(path)
    print(f"Creating {path} directory.")
    os.mkdir(path)

# Recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
def recurse_copy_dir(source,destination):
    wipe_dir(destination)
    # Copy all files and subdirectories, nested files, etc.
    if os.path.exists(source):
        if os.path.isdir(source):
            children = os.listdir(source)
            print(f"List of items inside {source}: {children}")
            # Recursion
            for child in children:
                full_path = os.path.join(source,child)
                if os.path.isdir(full_path):
                    full_des_path = os.path.join(destination,child)
                    recurse_copy_dir(full_path,full_des_path)
                    continue
                print(f"Copying {full_path} to {destination}")
                shutil.copy(full_path,destination)
        else:
            raise NotADirectoryError(f"{source} is not a directory.")
    else:
        raise FileNotFoundError(f"{source} does not exist.")



main()