#!/usr/bin/python

import sys
import re
import shutil
import os
import pdf2image
import subprocess

# extract equation, convert to image and creates a duplicate file with the link of online images

name = sys.argv[1].strip(".").strip("\\")


ipynb_header = """{
    "cells":[
        {"cell_type":"markdown","metadata":{},"source":[\""""

ipynb_footer = """"]}
    ],
    "metadata": {
      "kernelspec": {
       "display_name": "Python 3",
       "language": "python",
       "name": "python3"
      },
      "language_info": {
       "codemirror_mode": {
        "name": "ipython",
        "version": 3
       },
       "file_extension": ".py",
       "mimetype": "text/x-python",
       "name": "python",
       "nbconvert_exporter": "python",
       "pygments_lexer": "ipython3",
       "version": "3.6.6"
      }
     },
     "nbformat": 4,
     "nbformat_minor": 2
}
"""

def to_notebook(image_name, latex):
    with open("resources/"+image_name+".ipynb","w+") as f:
        f.write(ipynb_header+latex+ipynb_footer)


def create_gist(file_path):
    output = subprocess.check_output(['gh', 'gist', 'create', 'resources/'+file_path])
    # print("url: "+str(output)[2:-3])
    # print(type(output))
    return str(output)[2:-3]


os.chdir(name)
with open("main.md", 'r') as file:
    lines = file.readlines()

i=0
for index, line in enumerate(lines):
    if line[:2] == "$$" == line[-2:]:
        to_notebook("equation"+str(i), re.sub(r"\\",r"\\\\",line))
        # TODO: do something like this
        url = create_gist("equation"+str(i)+".ipynb")
        lines[index] = '<script src="'+url+'"></script>'
        lines[index] = '<embed type="text/x-python" src='+url+'>'
        i+=1

with open("tmp.md", "w") as file:
    file.writelines(lines)


with open("tmp.md", 'r') as file:
    lines = file.readlines()

gh_raw_url = "https://raw.githubusercontent.com/henridb/medium-articles/master/"+name+"/"

for index, line in enumerate(lines):
    lines[index] = re.sub("(resources/.*.png)", gh_raw_url+"\\1", line)

with open("tmp.md", 'w') as file:
    file.writelines(lines)