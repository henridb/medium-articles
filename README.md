# medium-articles

This repo contains my Medium articles in a Markdown format. This format is deemed
(by me) to be more flexible and easy to work with. It also allows me to work
offline. 

## Dependancies

In order to make a good use of this repo, you should have the following programs:
- python 3
- git (with a configured git account)
- the following python libraries:
	+ mdium
	+ pdf2image

## How it works

For now, the commands to call are in the `make.bat` file, which makes it a
Windows only "program". A CMake implementation may be coming to support other
OSs. The article to be published should be in a foler called `<name>`, and the
article itself should be called `main.md`. The upload is done by calling 
`make <name>` from the root of this repo.

This program will convert LaTeX equations (surrounded by `$$`) to images so they
are correctly displayed on Medium (Medium not supporting any ways to write
math...), these images are upladed to github, and in a temporary file, the
equations are replaced by the images (with the GitHub URL as source). This
temporary file is them uploaded to Medium using their API (through the mdium
python library).

For now, inline equations are not supported, but since inline images are not
supported on Medium, this is not really my fault ^^". Other features could be
added latter on, such as GitHub gists for code snippet, support for tables,
etc...

For now, complex formulas are not inlined, and simple ones will simply be
written using Unicode characters. Most of the equations is left in the LaTeX
format in the Markdown file, and tThe problem is then solved using the
`TeX to Unicode` extention, in the Medium editor. It has to be done in the Medium
editor because the Medium Markdown parser handles poorly Unicode exponents: if
Unicode exponents are in the markdown, the result will be quite random... But
even this solution is not perfect, because the extention can't handle "complex"
symbols, for example `\sqrt` and `\ldots` are not supported. To handle those, a
TeX to Unicode plugin is used in my IDE... (It's a shitty solution, I know, I
work with the limitation of the tools I have to use :/)

Finally, it may even be preferable to write your articles in LaTeX, a pipeline
could be created, using the software pandoc: to transform LaTex to Markdown, and
then upload Markdown to Medium. The command to transform LaTex to Markdown using
pandoc would look like `pandoc -s <your_file_name>.tex -o <your_file_name>.md`.
(
```
pandoc -t markdown_strict --citeproc -t markdown-citations -s <myfile>.tex -o main.md --bibliography <bib>.bib
```
could even be better: it converts the equations to UTF-8 and includes the 
referenced, but I personaly do not like the references format)

Any help to improve this is apreceated!

## Various notes

Mdium (https://github.com/icyphox/mdium) as is doesn't
support utf-8 character set, but adding `encoding="utf8"` on line 39 of the main
script aliviates that problem.