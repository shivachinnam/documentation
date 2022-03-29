import os
import subprocess

ignored_files_cmd = "find ./content/en -type f -name '*.md'  | git check-ignore --stdin | head -5"
ignored_md_files = subprocess.check_output(ignored_files_cmd, shell=True)
ignored_md_files_str = ignored_md_files.decode('UTF-8')

print(ignored_md_files_str)
print(type(ignored_md_files_str))
