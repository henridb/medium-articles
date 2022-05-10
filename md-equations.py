#!/usr/bin/python
# extract equation, convert to image and creates a duplicate file with the link of online images

import sys
import re
import os
from latex2svg import latex2svg

name = sys.argv[1].strip(".").strip("\\")

os.chdir(name)
with open("main.md", 'r') as file:
    lines = file.readlines()

i=0
for index, line in enumerate(lines):
    if line[:2] == "$$" == line[-2:]:
        with open("resources/equation"+str(i)+".svg","w") as file:
            file.writelines(latex2svg(line)['svg'])
        lines[index] = '<img src="resources/equation'+str(i)+'.svg" style="height:2em">'
        i+=1

with open("tmp.md", "w") as file:
    file.writelines(lines)


with open("tmp.md", 'r') as file:
    lines = file.readlines()

gh_raw_url = "https://raw.githubusercontent.com/henridb/medium-articles/master/"+name+"/"

for index, line in enumerate(lines):
    lines[index] = re.sub("(resources/.*.(png|svg))", gh_raw_url+"\\1", line)

with open("tmp.md", 'w') as file:
    file.writelines(lines)