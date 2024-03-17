block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"






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

def block_to_block_type(block):
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code
    lines = block.split("\n")
    all_lines_startswith_quote = True
    for line in lines:        
        if line.startswith(">"):
            continue
        else:
            all_lines_startswith_quote = False
            break
    if all_lines_startswith_quote:
        return block_type_quote
    all_lines_startswith_unordered = True
    for line in lines:
        if  line.startswith("*") or line.startswith("-"):
            continue
        else:
            all_lines_startswith_unordered = False
            break
    if all_lines_startswith_unordered:
            return block_type_unordered_list
    all_lines_startswith_ordered = True
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}."):
            all_lines_startswith_ordered = False
            break
    if all_lines_startswith_ordered:
        return block_type_ordered_list
    else:
        return block_type_paragraph