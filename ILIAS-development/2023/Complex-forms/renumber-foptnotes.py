import re
import os

def list_and_select_md_files():
    while True:
        # Get the current directory
        current_directory = os.getcwd()

        # List all files in the current directory with the .md extension
        md_files = [file for file in os.listdir(current_directory) if file.endswith(".md")]

        # Display numbered list of .md files
        print("List of Markdown files:")
        for i, md_file in enumerate(md_files, 1):
            print(f"{i}. {md_file}")

        # Prompt user for selection
        selected_index = input("Enter the number corresponding to the file you want to select: ")

        try:
            # Convert user input to integer
            selected_index = int(selected_index)

            # Validate the selected index
            if 1 <= selected_index <= len(md_files):
                selected_file = md_files[selected_index - 1]
                return selected_file
            else:
                print("Invalid selection. Please enter a valid number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def find_all_footnotes(markdown_text):
    footnote_pattern = re.compile(r'\[\^(\w+)\]')
    existing_footnotes = sorted(set(match for match in footnote_pattern.findall(markdown_text)))
    return existing_footnotes

def map_new_footnote_numbers(existing_footnotes):
    current_number = 1
    correct_by = 0
    searching = True
    map = {}
    while searching:
        if str(current_number) in existing_footnotes:
            map[str(current_number)] = str(current_number + correct_by)
            if str(current_number) + "B" in existing_footnotes:
                correct_by += 1
                map[str(current_number) + "B"] = str(current_number + correct_by)
        else:
            searching = False
        current_number += 1
    return map

def replace_footnotes_by_map(text, footnote_map):
    for key, value in footnote_map.items():
        # Use re.sub with word boundaries to match whole words
        text = re.sub(r'\b\[\^' + re.escape(key) + r'\]\b', f'[^{value}]', text)
        print(f"[^{key}] [^{value}]")
    return text

markdown_file = list_and_select_md_files()

with open(markdown_file, 'r', encoding='utf-8') as file:
    markdown_text = file.read()
existing_footnotes = find_all_footnotes(markdown_text)
print(existing_footnotes)
footnote_map = map_new_footnote_numbers(existing_footnotes)
print(footnote_map)
new_markdown = replace_footnotes_by_map(markdown_text, footnote_map)

with open(markdown_file.replace(".md", "_renumbered-footnotes.md"), 'w', encoding='utf-8') as file:
    file.write(new_markdown)