"""
Simple File Organizer

Organizes files in a folder based on file extension.

Author: Kiran
"""

import os
import shutil

folder_path = "files"

if not os.path.exists(folder_path):
    print("Folder not found.")
else:
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):

            if "." in file_name:
                extension = file_name.split(".")[-1]
            else:
                extension = "others"

            new_folder = os.path.join(folder_path, extension)

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)

            new_path = os.path.join(new_folder, file_name)
            shutil.move(file_path, new_path)

    print("Files organized successfully.")
