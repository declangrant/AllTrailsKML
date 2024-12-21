import argparse
import os
import traceback

from data_extractor import extract_data_from_file
from data_to_kml import data_json_to_kml
from path_helpers import INPUT_PATH, EXTRACTED_PATH, OUTPUT_PATH


# create argument parser with usage help
parser = argparse.ArgumentParser(description="AllTrails to KML")
parser.add_argument(
    "files", nargs="*",
    help="files to process, relative to the input folder"
)
parser.add_argument(
    "-i", "--init", action="store_true",
    help="create the input/output folders and exit"
)
args = parser.parse_args()

# do initialization action
if args.init:
    print("creating folders...")
    # create folders only if they don't exist
    if not os.path.exists(INPUT_PATH):
        os.makedirs(INPUT_PATH)
        print(" ", INPUT_PATH)
    if not os.path.exists(EXTRACTED_PATH):
        os.makedirs(EXTRACTED_PATH)
        print(" ", EXTRACTED_PATH)
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
        print(" ", OUTPUT_PATH)
    # exit the program
    print("done")
    exit(0)

# do file processing action
if args.files:
    file_names = args.files
else:   # read all files if none supplied
    file_names = os.listdir(INPUT_PATH)

print("processing files...")
errors = []
for file_name in file_names:
    # process all files, even if some fail
    try:
        print(" ", file_name, end="")
        extract_data_from_file(file_name)
        data_json_to_kml(file_name+".json")
        print()
    except:
        print("\t", "ERROR")
        errors.append(traceback.format_exc())
# show errors
if errors:
    print("some errors occurred:\n")
    for ex in errors:
        print(ex)
    exit(1)
else:
    print("done")
