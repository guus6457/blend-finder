import os
import shutil

def copy_blend_files(download_folder, destination_folder):
    # Check if download folder exists
    if not os.path.exists(download_folder):
        print("Download folder does not exist.")
        return

    # Check if destination folder exists, if not create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get list of files in download folder
    files = os.listdir(download_folder)

    # Filter .blend files
    blend_files = [f for f in files if os.path.isfile(os.path.join(download_folder, f)) and f.endswith('.blend')]

    if not blend_files:
        print("No .blend files found in the download folder.")
        return

    # Copy .blend files to destination folder
    for blend_file in blend_files:
        src = os.path.join(download_folder, blend_file)
        dst = os.path.join(destination_folder, blend_file)
        shutil.copyfile(src, dst)
        print(f"Copied {blend_file} to {destination_folder}")

# Set your download folder path and destination folder path
download_folder = "/path/to/your/download/folder"
destination_folder = "/path/to/your/destination/folder"

# Call the function to copy .blend files
copy_blend_files(download_folder, destination_folder)
