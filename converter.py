from pathlib import Path
import sys
from PIL import Image
import re


def get_user_paths():
    try:
        return {
            "input_path": Path(sys.argv[1]),
            "output_path": Path(sys.argv[2])
        }
    except IndexError:
        print("Provide the output and output folders")


user_paths = get_user_paths()


def output_exists_or_create():
    if (not user_paths["output_path"].exists()):
        Path.mkdir(user_paths["output_path"])
        print(f'Created {user_paths["output_path"]} folder')


output_exists_or_create()


def convert_to_png():
    # Get every jpg in the input directory
    input_directory_files = list(Path(user_paths["input_path"]).glob("*.jpg"))
    files_count = len(input_directory_files)

    print(f"Found {files_count} jpg files in the input folder")

    completed = 0
    for img_path in input_directory_files:
        with Image.open(img_path) as img:
            img_filename = re.search(
                r'[^\\/:*?"<>|\r\n]+$', img.filename).group()
            img_output_path = (user_paths["output_path"] /
                               img_filename.replace("jpg", "png"))
            img.save(img_output_path, "png")
            completed += 1
            print(f"Completed {completed}/{files_count}")
    print("All the images converted to png!")


convert_to_png()
