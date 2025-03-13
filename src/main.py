from markdown_blocks import *
import os,shutil

def main():
    wipe_dir("./public")
    recurse_copy_dir("./static","./public")
    generate_page("./content/index.md","./template.html","./public/index.html")

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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path,'r') as file: # 'r' is default & the file will only be read
        md_contents = file.read()
    with open(template_path) as file: # 'r' is default & the file will only be read
        template_contents = file.read()

    html_string = markdown_to_html_node(md_contents).to_html()
    title = extract_title(md_contents)

    full_html_page = (template_contents.replace("{{ Title }}",title)).replace("{{ Content }}",html_string)

    with open(dest_path,'w') as file: # 'w' for only writing (an existing file with the same name will be erased)
        file.write(full_html_page)


main()