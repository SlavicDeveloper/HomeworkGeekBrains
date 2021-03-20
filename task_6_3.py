import os
import shutil

root_dir = "my_project_2"
dir_name = "templates"

for root, dir, files in os.walk(root_dir):
    if root.find(dir_name) > 0:
        shutil.copytree(root, dir_name)











