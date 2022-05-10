# Gist Creation From Markdown File
# from https://medium.com/deena-does-data-science/jupyter-notebook-extensions-e6b57d004e8e

# import libraries
import re
from pathlib import Path
import argparse
import requests
import json

# Set up variables
GIST_TOKEN_PATH = "create_gist_token.txt"
GITHUB_ID = 'henridb'
PY_CODEBLK_PAT =  '```python\n'
END_CODEBLK_PAT = '```'
FILE_EXT = ".py"
MD_EXT = ".md"
MD_FILES = [f for f in Path(".").iterdir() if f.suffix == MD_EXT]

# Read & Parse args
my_parser = argparse.ArgumentParser(prog='gistmark', description='Gist the code blocks in MarkDown file')
my_parser.add_argument('file', action='store', nargs='?', default=MD_FILES[0])
my_parser.add_argument('token', action='store', nargs='?', default=GIST_TOKEN_PATH)
args = my_parser.parse_args()

# Display the file name
mdFile = Path(args.file)
tokenFile = Path(args.token)
print(f'Gisting the file: {mdFile}')

# Read the contents of the file
assert mdFile.is_file(), "Markdown file does not exist"
assert mdFile.suffix == MD_EXT, "Input file must be of extenstion: '.md'"
with open(mdFile, 'r') as f:
    content = f.read()

# Get all code snippets from the file
def getCodeSnippets(code):
    # Flag re.S searches across mutiple lines
    return re.findall(PY_CODEBLK_PAT + '(.*?)' + END_CODEBLK_PAT, code, re.S)
codeSnippets = getCodeSnippets(content)
nrSnippets = len(codeSnippets)
assert nrSnippets > 0, 'No Code Snippets found!'
print(f'{nrSnippets} of code snippets found.')

# Get the first comment from code snippet
def getSnippetName(code, ext = FILE_EXT): 
    name = code.split("\n")[0].strip()
    assert name[0] == "#", "Please name the code snippet using '#'"
    return name.strip("#").strip().replace(" ", "_") + ext

# Set the first comment of the code snippet as file name of the snippet
gists = {}
for code in codeSnippets: gists[getSnippetName(code)] = { "content": code }


# Get the first header of the Markdown file
# This will be set as description of the gist
def getDesc(txt):
    return re.findall(r'#(.*?)\n', txt)[0].strip()

# Get the gist creation token
assert tokenFile.is_file(), "token file does not exist"
with open(tokenFile, 'r') as f: token = f.read().strip('\n')

# Set up the data to be uploaded
query_url = "https://api.github.com/gists"
data = {
    "public": True,
    "description": getDesc(content),
    "files": gists
}
headers = {'Authorization': f'token {token}'}

# Send the request
req = requests.post(query_url, headers=headers, data=json.dumps(data))
assert req.ok, 'Github API call failed'

# Get the gist embedding for Medium
def mediumGist(req, file):
    gisturl = req.json()['html_url']
    url = gisturl + '.js?file=' + file
    return url

# Get the liquid text of the gist for Dev Community    
def devGist(req, file, username = GITHUB_ID):
    id = req.json()["id"]
    url = f'gist https://gist.github.com/{username}/{id}'
    return f'{{% {url} file={file} %}}'

# Replace the code blocks with corresponding gist in the Markdown file 
updatedContent = content
# Loop through all files
for fileName in list(gists.keys()):
    # Get the content which was uplaoded for this file
    codeSnippet = PY_CODEBLK_PAT + req.json()['files'][fileName]['content'] + END_CODEBLK_PAT
    # Set the link as the combination of DevCommunity & Medium gists
    link = devGist(req, fileName) + "\n\n" + mediumGist(req, fileName)
    # Replace the orginal content with 
    updatedContent = updatedContent.replace(codeSnippet, link)

# Write the updated Markdown file to disk
updateFileName = mdFile.with_name("Gist_" + mdFile.stem + MD_EXT)
with open(updateFileName,'w+') as f:
    f.write(updatedContent)
print(f'Created the file: {updateFileName.name}')