"""
Step one upload file using document_uploader.py
"""

"""
Step Two extract headings and copy them from console and paste them onto the section titles list.
"""
import re


def get_headings(file_name):
    """
    Extract headings from a txt file.
    """
    with open(file_name, 'r') as f:
        text = f.read()
    headings = re.findall(r'#+\s*(.*)', text)
    return headings


print(get_headings('Insurance_act_18.txt'))

"""
Step three split titles into keys and  values. To get the index numbers to populate the html and css code.
"""
section_titles = []
split_list_keys = []

for keys in section_titles:
    key = keys.split(".", 1)
    split_list_keys.append(key)

print(split_list_keys)
