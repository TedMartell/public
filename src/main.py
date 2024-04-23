import os
import shutil
from textnode import TextNode

def copy_dir(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        if os.path.isfile(os.path.join(source, item)):
            shutil.copy(os.path.join(source, item), destination)
        else:
            copy_dir(os.path.join(source, item), os.path.join(destination, item))

def main(): 
    source_dir = '../static'  # Note the '/': It's '../static', not '..static'
    destination_dir = '../public'  # Similarly, ensure it's '../public'
    copy_dir(source_dir, destination_dir)
    print("Copying complete!")


if __name__ == "__main__":
    main()


        