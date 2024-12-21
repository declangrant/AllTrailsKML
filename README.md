# AllTrails to KML

This program extracts trails (including waypoints) from the AllTrails map editor and saves them as KML files.

## Installation

This program is written in Python, and this guide assumes you have Python 3 installed. This program also requires two third-party Python libraries:
- [`polyline`](https://github.com/frederickjansen/polyline) for decoding the trail data
- [`simplekml`](https://github.com/eisoldt/simplekml) for building the KML files

These can be installed using `pip`:
```
$ pip install polyline simplekml
```

Once you have these, download or clone this repo. Enter the program folder and run the program in initialization mode to create the necessary folders:
```
$ python alltrails.py -i
```

## Usage

To process all files in the input folder, run:
```
$ python alltrails.py
```

To process a single file or list of files, run:
```
$ python alltrails.py trail1.html 'trail 2.html'
```

### Downloading Maps

This program is not capable of getting map data directly from [alltrails.com](https://www.alltrails.com). Instead, you must copy map editor source HTML to the input folder.

1. Find a trail to download.
1. Open the map for that trail.
1. Click the edit button in the bottom right corner of the page.
1. View page source (right click anywhere outside the map area, or Ctrl+U in Chrome)
1. Copy the HTML to a file in the input folder.
