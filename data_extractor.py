import re
import json
import os
import sys

from path_helpers import INPUT_PATH, EXTRACTED_PATH


def extract_data_from_file(file_name: str) -> None:
    """
    Extracts JSON data from the SearchApp class of an AllTrails map editor. The
    file is read from the `1.input` folder and written to the `2.extracted`
    folder with the same file name.

    Args:
        file_name: Name of the input file relative to `1.input`. If the file
            has an extension, it must be included.
    """
    # read file contents
    with open(INPUT_PATH+file_name, "r", encoding="utf-8") as file:
        file_content = file.read()
    # extract editor data
    data_match = re.search('<div data-react-class="SearchApp" data-react-props="({.+})"', file_content)
    if data_match is None:
        raise ValueError("Could not find data")
    # parse as json
    data = json.loads(data_match.group(1).replace('&quot;', '"'))
    # write extracted data
    with open(EXTRACTED_PATH+file_name+".json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# if running this file directly
if __name__ == "__main__":
    # no args provided, run for all files
    if len(sys.argv) == 1:
        for file_name in os.listdir(INPUT_PATH):
            extract_data_from_file(file_name)
    # assume all args are one file name, with spaces
    else:
        extract_data_from_file(" ".join(sys.argv[1:]))
