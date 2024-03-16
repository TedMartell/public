import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, bold section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)

def split_nodes_image(old_nodes):
    new_nodes = []
    if old_nodes == []:
        return []
    for old_node in old_nodes:
        split_nodes = []
        if extract_markdown_images(old_node.text) == []:
            new_nodes.append(old_node)
        images = extract_markdown_images(old_node.text)
        remaining_text = old_node.text
        for i in range(len(images)):
            sections = remaining_text.split(f"![{images[i][0]}]({images[i][1]})", 1)
            remaining_text = sections[1]
            if sections[0] != "":
                split_nodes.append(TextNode((sections[0].strip()), text_type_text))
            if images[i][0] != "":
                split_nodes.append(TextNode((images[i][0].strip()), text_type_image, images[i][1]))
        if remaining_text != "":
            split_nodes.append(TextNode(remaining_text.strip(), text_type_text))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    if old_nodes == []:
        return []
    for old_node in old_nodes:
        split_nodes = []
        if extract_markdown_links(old_node.text) == []:
            new_nodes.append(old_node)
        links = extract_markdown_links(old_node.text)
        remaining_text = old_node.text
        for i in range(len(links)):
            sections = remaining_text.split(f"[{links[i][0]}]({links[i][1]})", 1)
            remaining_text = sections[1]
            if sections[0] != "":
                split_nodes.append(TextNode((sections[0].strip()), text_type_text))
            if links[i][0] != "":
                split_nodes.append(TextNode((links[i][0].strip()), text_type_link, links[i][1]))
        if remaining_text != "":
            split_nodes.append(TextNode(remaining_text.strip(), text_type_text))
        new_nodes.extend(split_nodes)
    return new_nodes





