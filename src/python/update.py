""" 
Python program to combine common html header with content files
"""

# from collections import namedtuple
import os
import re

SRC = os.path.realpath("./src")
PUBLIC = os.path.realpath("./public")
HTML = os.path.join(SRC, 'html')

class Page:
    def __init__(self, title, file_name):
        self.title = title
        self.file_name = os.path.join(HTML, file_name)
        self.public_file = os.path.join(PUBLIC, file_name)


def get_pages():
    pages = [Page(title="Home", file_name="home.html")]
    return pages


class Pages:
    def __init__(self, pages: list[Page]):
        # print(self.src_dir)
        self.pages = pages
        # self.names = ["Home", "About", "Module 1", "Contact"]
        self.template_file = os.path.join(HTML, "template.html")
        self.read_template()

    def read_template(self):
        try:
            with open(self.template_file, mode="r", encoding="utf-8") as f:
                self.template = f.read()
        except FileNotFoundError as err:
            print(err)
            raise FileNotFoundError
        except IOError as err:
            print(err)
            raise IOError

    def update(self):
        pattern = re.compile(r'^\s*<div class="template"></div>\s*$', re.MULTILINE)
        beginning_of_line = re.compile(r'^', re.MULTILINE)
        for page in self.pages:
            # read in the file
            try:
                with open(page.file_name, mode="r", encoding="utf-8") as f:
                    content = f.read()
                    # add 4 spaces before each line in the content
                    # content = re.sub(r'^', '    ', content, flags=re.MULTILINE)
                    content = beginning_of_line.sub('    ', content)
                    updated = pattern.sub(content, self.template)
                with open(page.public_file, mode='w+', encoding='utf-8') as f:
                    f.write(updated)
            except FileNotFoundError as err:
                print(err)
            except IOError as err:
                print(err)
            print(page.title)


pages = Pages(get_pages())
pages.update()
