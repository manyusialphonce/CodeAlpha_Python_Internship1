import os
import shutil

source_folder = "source"
destination_folder = "jpg_files"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )

print("All JPG files moved successfully.")