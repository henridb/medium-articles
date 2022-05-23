#!/usr/bin/python

import sys
import re
import shutil
import os
import pdf2image

# extract equation, convert to image and creates a duplicate file with the link of online images

name = sys.argv[1].strip(".").strip("\\")

def create_image_from_latex(image_name,latex):
    if "rough" not in os.listdir():
        os.mkdir("rough")
    with open("rough/a.tex","w+") as f:
        f.write(
            "\\documentclass[border=1pt]{standalone}"
            "\\usepackage{amsmath}\n"
            "\\begin{document}\n$"
            latex
            "$\n\\end{document}"
        )
    os.chdir("rough")
    os.system("pdflatex a.tex")
    os.chdir("..")
    image = pdf2image.convert_from_path("rough/a.pdf",size=(None,30),fmt="png")[0]
    image.save("resources/"+image_name+".png", "PNG")
    shutil.rmtree("rough")


os.chdir(name)
with open("main.md", 'r', encoding="utf8") as file:
    lines = file.readlines()

i=0
for index, line in enumerate(lines):
    print(index, line[:2], line[-3:-1])
    if line[:2] == "$$" == line[-3:-1]:
        create_image_from_latex("equation"+str(i),line[2:-3])
        lines[index] = '<img src="resources/equation'+str(i)+'.png" style="height:2em">'
        i+=1

with open("tmp.md", "w", encoding="utf8") as file:
    file.writelines(lines)


with open("tmp.md", 'r', encoding="utf8") as file:
    lines = file.readlines()

gh_raw_url = "https://raw.githubusercontent.com/henridb/medium-articles/master/"+name+"/"

for index, line in enumerate(lines):
    lines[index] = re.sub("(resources/.*.png)", gh_raw_url+"\\1", line)

with open("tmp.md", 'w', encoding="utf8") as file:
    file.writelines(lines)