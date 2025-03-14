import os
from markdown_blocks import markdown_to_blocks,markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,BASEPATH):
    if os.path.exists(dir_path_content):
        if os.path.isdir(dir_path_content):
            children = os.listdir(dir_path_content)
            # Recursion
            for child in children:
                full_src_path = os.path.join(dir_path_content,child)
                if os.path.isdir(full_src_path):
                    full_des_path = os.path.join(dest_dir_path,child)
                    os.mkdir(full_des_path)
                    generate_pages_recursive(full_src_path,template_path,full_des_path,BASEPATH)
                    continue
                generate_page(
                    full_src_path,
                    template_path,
                    os.path.join(dest_dir_path,"index.html"),
                    BASEPATH
                    )
        else:
            raise NotADirectoryError(f"{dir_path_content} is not a directory.")
    else:
        raise FileNotFoundError(f"{dir_path_content} does not exist.")

def generate_page(from_path, template_path, dest_path,BASEPATH):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path,'r') as file: # 'r' is default & the file will only be read
        md_contents = file.read()
    with open(template_path) as file: # 'r' is default & the file will only be read
        template_contents = file.read()

    html_string = markdown_to_html_node(md_contents).to_html()
    title = extract_title(md_contents)

    full_html_page = (template_contents.replace("{{ Title }}",title)).replace("{{ Content }}",html_string)
    # Update BASEPATH
    full_html_page = full_html_page.replace("href=\"/",f"href=\"{BASEPATH}")
    full_html_page = full_html_page.replace("src=\"/",f"src=\"{BASEPATH}")

    with open(dest_path,'w') as file: # 'w' for only writing (an existing file with the same name will be erased)
        file.write(full_html_page)

def extract_title(markdown):
    for block in markdown_to_blocks(markdown):
        if block.startswith("# "):
            return block[2:].strip()
    raise LookupError("No [h1] header found.")