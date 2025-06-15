import zipfile
import os

zip_filename = "app.zip"
folder_to_zip = "my-eb-app"

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_to_zip):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, folder_to_zip)
            zipf.write(filepath, arcname)

print(f"{zip_filename} created successfully.")
