import zipfile
import os

# Name of the zip file
zip_filename = "app.zip"

# Folder to zip (current directory)
folder_to_zip = os.getcwd()

# Create the zip file
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_to_zip):
        for file in files:
            if file == zip_filename:
                continue  # Skip the zip file itself
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, folder_to_zip)
            zipf.write(filepath, arcname)

print(f"Created {zip_filename} from {folder_to_zip}")
