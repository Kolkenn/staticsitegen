import os.path

from copystatic import wipe_dir,recurse_copy_dir
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print(f"Wiping {dir_path_public} directory...")
    wipe_dir(dir_path_public)

    print(f"Copying files in {dir_path_static} directory to {dir_path_public} directory...")
    recurse_copy_dir(dir_path_static,dir_path_public)
    
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public
        )

main()