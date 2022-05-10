#!/usr/bin/python

import sys
import re
import shutil
import os
import pdf2image

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