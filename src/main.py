import os.path
import sys

from copystatic import wipe_dir,recurse_copy_dir
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if len(sys.argv) > 1:
        BASEPATH = sys.argv[1]
    else:
        BASEPATH = "/"
    
    print(f"Wiping {dir_path_docs} directory...")
    wipe_dir(dir_path_docs)

    print(f"Copying files in {dir_path_static} directory to {dir_path_docs} directory...")
    recurse_copy_dir(dir_path_static,dir_path_docs)
    
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_docs,
        BASEPATH
        )

main()