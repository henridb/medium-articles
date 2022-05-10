#!/usr/bin/python

import sys
import re
import shutil
import os
import pdf2image

# extract equation, convert to image and creates a duplicate file with the link of online images

name = sys.argv[1].strip(".").strip("\\")


def to_notebook(image_name, latex):
    with open("resources/"+image_name+".ipynb","w+") as f:
        f.write('{"cells": [{"cell_type": "markdown", "metadata": {}, "source": ["'
            +latex+
            '"]}]}')


os.chdir(name)
with open("main.md", 'r') as file:
    lines = file.readlines()

i=0
for index, line in enumerate(lines):
    if line[:2] == "$$" == line[-2:]:
        to_notebook("equation"+str(i), re.sub(r"\\",r"\\\\",line))
        lines[index] = '<embed type="text/ipynb" src="resources/equation'+str(i)+'.ipynb" width="300" height="200">'
        i+=1

with open("tmp.md", "w") as file:
    file.writelines(lines)


with open("tmp.md", 'r') as file:
    lines = file.readlines()

gh_raw_url = "https://raw.githubusercontent.com/henridb/medium-articles/master/"+name+"/"

for index, line in enumerate(lines):
    lines[index] = re.sub("(resources/.*.(png|ipynb))", gh_raw_url+"\\1", line)

with open("tmp.md", 'w') as file:
    file.writelines(lines)