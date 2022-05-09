#!/usr/bin/python

import sys
import re
import shutil
import os
import pdf2image
from time import sleep
from PIL import Image

# extract equation, convert to image

name = sys.argv[1].strip(".").strip("\\")

def create_image_from_latex(image_name,latex):
    if "rough" not in os.listdir():
        os.mkdir("rough")
    with open("rough/a.tex","w+") as f:
        f.write("\\documentclass[border=1pt]{standalone}\n\\begin{document}\n$"+
            latex+
            "$\n\\end{document}")
    os.chdir("rough")
    os.system("pdflatex a.tex")
    os.chdir("..")
    image = pdf2image.convert_from_path("rough/a.pdf",size=(None,500),fmt="png")[0]
    image.save("resources/"+image_name+".png", "PNG")
    shutil.rmtree("rough")


os.chdir(name)
with open("main.md", 'r') as file:
    lines = file.readlines()

i=0
for index, line in enumerate(lines):
    if line[:2] == "$$" == line[-2:]:
        create_image_from_latex("equation"+str(i),line[2:-2])
        lines[index] = '<img src="resources/equation'+str(i)+'.png" style="height:2em">'
        i+=1

with open("tmp.md", "w") as file:
    file.writelines(lines)


with open("tmp.md", 'r') as file:
    lines = file.readlines()

gh_raw_url = "https://raw.githubusercontent.com/henridb/medium-articles/master/"+name+"/"

for index, line in enumerate(lines):
    lines[index] = re.sub("(resources/.*.png)", gh_raw_url+"\\1", line)

print(lines)

with open("tmp2.md", 'w') as file:
    file.writelines(lines)