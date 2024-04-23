import os
from htmlnode import LeafNode, ParentNode, HTMLNode
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    with open(template_path, "r") as file:
        markdown_template = file.read()
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    html_title = extract_title(markdown_content)
    html_page = markdown_template.replace("{{ Title }}", html_title)
    html_page = html_page.replace("{{ Content }}", html_content)
    destination_dir = os.path.dirname(dest_path)
    os.makedirs(destination_dir, exist_ok=True)
    with open(dest_path, 'w') as output_file:
        output_file.write(html_page)




