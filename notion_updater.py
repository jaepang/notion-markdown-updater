import os
from datetime import datetime
from pytz import timezone

from config import *

def parse_language(lan):
    lan = lan.lower()
    if lan == 'c++':
        lan = 'cpp'
    elif lan == 'c#':
        lan = 'csharp'
    elif lan == 'objective-c':
        lan = 'objectivec'
    return lan

def post_to_markdown(post, depth):
    text = ""
    if depth == 0:
        # Handle Frontmatter
        text += "---\ntitle: %s\ndate: %s\ndescription: %s\n---" % (post.title, post.created, post.description)
        # Handle Title
        text += "\n\n" + "# " + post.title + "\n\n"
    numered_list_index = 1
    bullet = False

    for block in post.children:
        for i in range(0, depth):
            text += "\t"
        # Handles Numbered List
        if block.type == "numbered_list":
            text += str(numered_list_index) + ". " + block.title + "\n"
            numered_list_index += 1
        else:
            if numered_list_index > 1:
                text += "\n"
            numered_list_index = 1
        # Handles Bullets List
        if block.type == "bulleted_list":
            text += "- " + block.title + "\n"
            bullet = True
        else:
            if bullet:
                text += "\n"
            bullet = False
        # Handles H1
        if block.type == "header":
            text += "# " + block.title + "\n\n"
        # Handles H2
        if block.type == "sub_header":
            text += "## " + block.title + "\n\n"
        # Handles H3
        if block.type == "sub_sub_header":
            text += "### " + block.title + "\n\n"
        # Handles Code Blocks
        if block.type == "code":
            text += "``` " + parse_language(block.language) + "\n" + block.title + "\n```\n\n"
        # Handles Images
        if block.type == "image":
            text += "![" + block.id + "](" + block.source + ")\n\n"
        # Handles Dividers
        if block.type == "divider":
            text += "---" + "\n"
        if block.type == "bookmark":
            text += "[" + block.title + "](" + block.link + ")\n\n"
        # Handles Basic Text, Links, Single Line Code
        if block.type == "text":
            text += block.title + "\n\n"
        # Handle Nested Block
        children = block.children
        if bool(children):
            text += post_to_markdown(block, depth+1)
    return text

def write_file(post, text):
    title = post.title.replace(" ", "-")
    title = title.replace(".", "")
    title = title.replace(",", "")
    title = title.replace(":", "")
    title = title.replace(";", "")
    title = title.lower()
    try:
        os.mkdir(post_path + title)
    except:
        pass
    # Fix here with your own path and format of your blog:
    file = open(post_path + title + "/index.md", 'w')
    file.write(text)

def update_row(post):
    text = post_to_markdown(post, 0)
    write_file(post, text)

if __name__ == "__main__":
    new_publish = False
    for post in posts:
        if post.status == publish_ready:
            update_row(post)
            post.status = published
            print(datetime.now(timezone=timezone_log).strftime('%Y-%m-%d %H:%M:%S'), ": updated \"%s\"" % post.title, sep="")
            new_publish = True
    if auto_deploy and new_publish:
        # auto_deploy
        print(datetime.now(timezone=timezone_log).strftime('%Y-%m-%d %H:%M:%S'), ": deploy start", sep="")