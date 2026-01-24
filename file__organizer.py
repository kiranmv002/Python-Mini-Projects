# Simple File Organizer
# Organizes files in a folder based on file extension

import os
import shutil

folder_path = "files"

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        extension = file_name.split(".")[-1]

        new_folder = os.path.join(folder_path, extension)

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        shutil.move(file_path, os.path.join(new_folder, file_name))

print("Files organized successfully.")
