import re


def get_headings(file_name):
    """
    Extract headings from a txt file.
    """
    with open(file_name, 'r') as f:
        text = f.read()
    headings = re.findall(r'#+\s*(.*)', text)
    return headings


def extract_headings(text):
    """
    extract headings marked #.
    """
    return re.findall(r'#+\s*(.*)', text)


def extract_sub_headings(text):
    """
    extract sub_headings marked ##.
    """
    return re.findall(r'#-+\s*(.*)', text)


def extract_paragraphs(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        paragraphs = re.findall(r'(?<=#\\)(.*?)(?=#\\)', text, re.DOTALL)
        return paragraphs


def remove_comments(text):
    return re.sub(r'#.*', '', text)


def delete_comments(text):
    return re.sub(r'#.*', '', text)


# content = []
#
# with open('New_FAIS.txt') as file:
#     print(extract_headings(file.readlines()))

# print(content)

paragraphs_list = []
for paragraph in extract_paragraphs('Insurance_act_18.txt'):
    print(paragraph)
    paragraphs_list.append(paragraph)
print(paragraphs_list[0][0])

# cleaned_list = []
# for paragraph in paragraphs_list:
#     print(delete_comments(paragraph))
# print(paragraph)
# heading = extract_headings(paragraph)
# print(heading)
# sub_heading = extract_sub_headings(paragraph)
# print(sub_heading)
# final_paragraph = delete_comments(paragraph)
# print(final_paragraph)
# finalised = heading, final_paragraph
# cleaned_list.append(finalised)

# for head in cleaned_list[0][0]:
#     print(head)
# print(cleaned_list[0][1])

# if __name__ == '__main__':
#     print(get_headings('Insurance_act_18.txt'))
# print(extract_paragraphs('FAIS.txt'))
# print(paragraphs_list[0])
