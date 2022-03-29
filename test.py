import os
import subprocess

ignored_files_cmd = "find ./content/en -type f -name '*.md'  | git check-ignore --stdin"
cmd_output = subprocess.check_output(ignored_files_cmd, shell=True)
ignored_md_files = cmd_output.decode('UTF-8').strip().split('\n')
ignored_md_files_list = list()

for file_path in ignored_md_files:
    open_file = open(file_path, 'r')
    content = open_file.read()
    content_dict = dict(file_path=file_path, content=content)
    ignored_md_files_list.append(content_dict)
