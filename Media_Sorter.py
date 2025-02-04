import os
import shutil
from datetime import datetime
import platform
from PIL import Image
from PIL.ExifTags import TAGS

def create_folder(directory):
    """Create a folder if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_photo_taken_date(file_path):
    """Extract the date the photo or video was taken from metadata, if available."""
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == 'DateTimeOriginal':
                        return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception:
        pass
    return None


def get_creation_date(file_path):
    """Get the creation date of a file, prioritizing creation date over modified date."""
    if platform.system() == 'Windows':
        creation_time = os.path.getctime(file_path)
    else:
        stat = os.stat(file_path)
        try:
            creation_time = stat.st_birthtime
        except AttributeError:
            creation_time = stat.st_ctime
    return datetime.fromtimestamp(creation_time)


def sort_files_by_date(source_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    sorted_folder = os.path.join(source_folder, 'Sorted')
    create_folder(sorted_folder)

    media_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mov', '.avi', '.mkv','.3gp','.webm']

    while True:
        try:
            start_date_input = input("Enter start date (DD-MM-YYYY) or type 'end' to stop: ")
            if start_date_input.lower() == 'end':
                break

            start_time_input = input("Enter start time (HH:MM): ")
            end_time_input = input("Enter end time (HH:MM): ")

            start_datetime = datetime.strptime(f"{start_date_input} {start_time_input}", '%d-%m-%Y %H:%M')
            end_datetime = datetime.strptime(f"{start_date_input} {end_time_input}", '%d-%m-%Y %H:%M')

            folder_name = input("Enter the folder name: ")
            folder_path = os.path.join(sorted_folder, folder_name)
            create_folder(folder_path)

            for root, _, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    if not any(file.lower().endswith(ext) for ext in media_extensions):
                        continue

                    taken_date = get_photo_taken_date(file_path)
                    if not taken_date:
                        taken_date = get_creation_date(file_path)

                    if start_datetime <= taken_date <= end_datetime:
                        shutil.move(file_path, os.path.join(folder_path, file))
                        print(f"Moved {file} to {folder_path}")

            print(f"Files moved to {folder_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    print("Sorting completed.")


if __name__ == "__main__":
    # Use environment variable to find Desktop path
    user_profile = os.environ.get('USERPROFILE') or os.environ.get('HOME')
    
    # Define the default source folder to the user's Desktop
    source_folder = os.path.join(user_profile, "Desktop", "Photos To Sort")
    
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
    else:
        sort_files_by_date(source_folder)
