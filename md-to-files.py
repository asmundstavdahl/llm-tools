#!/bin/env python3

import re
import os
import sys


def parse_markdown_and_save_files(markdown_content):
    # Regular expression to match code blocks and file names
    pattern = re.compile(r"#### File: `(.*?)`\n.*?```(.*?)\n(.*?)\n```", re.DOTALL)

    matches = pattern.findall(markdown_content)
    for match in matches:
        file_path = match[0].strip()
        code_language = match[1].strip()
        code_content = match[2].strip()

        print(f"Creating {file_path}... ", end="")

        # Create the directory if it doesn't exist
        dir = os.path.dirname(file_path)
        if dir != "":
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the code content to the file
        with open(file_path, "w") as file:
            file.write(code_content)

        print("done")


# Read the markdown content from STDIN
markdown_content = sys.stdin.read()

parse_markdown_and_save_files(markdown_content)
