def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n")
    block = ""
    for line in lines:
        if line.strip() != "":
            if block != "":
                block += "\n" + line
            else:
                block = line
        elif block.strip() != "":
            blocks.append(block.strip())
            block = ""         
    return blocks