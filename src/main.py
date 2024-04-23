import os
import shutil
from generate_page import generate_pages_recursive
# Assuming textnode is a module you're using somewhere

def copy_dir(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination, exist_ok=True)  # Using makedirs with exist_ok=True is safer
    for item in os.listdir(source):
        s_item = os.path.join(source, item)
        d_item = os.path.join(destination, item)
        if os.path.isfile(s_item):
            shutil.copy(s_item, destination)
        else:
            copy_dir(s_item, d_item)

def main(): 
    source_dir = '../static'  # Note: Check these paths, they may need adjustment based on your project structure
    destination_dir = '../public'
    dir_path_public = "../public"
    dir_path_content = "../content"
    template_path = "../template.html"
    copy_dir(source_dir, destination_dir)
    print("Copying static files complete!")

    
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)



if __name__ == "__main__":
    main()



        