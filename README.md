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
	+ shutil

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

Finally, it may even be preferable to write your articles in LaTeX, a pipeline
could be created, using the software pandoc: to transform LaTex to Markdown, and
then upload Markdown to Medium. The command to transform LaTex to Markdown using
pandoc would look like `pandoc -s <your_file_name>.tex -o <your_file_name>.md`.

Any help to improve this is apreceated!