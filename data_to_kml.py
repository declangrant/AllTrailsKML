import json
import polyline
import simplekml
import os
import sys

from path_helpers import EXTRACTED_PATH, OUTPUT_PATH


def data_json_to_kml(file_name: str) -> None:
    """
    Creates a KML file from the route and waypoint data in an extracted JSON
    file. The file is read from the `2.extracted` folder and written to the
    `3.output` folder with the name of the trail as the file name.

    Args:
        file_name: Name of the input file relative to `2.extracted`.
    """
    # load extracted data
    with open(EXTRACTED_PATH+file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    # initiate kml builder
    kml = simplekml.Kml()
    kml.document.name = data["initialExploreMap"]["name"]
    kml.document.description = data["initialTrackTrailResult"].get("description_source", data["initialTrackTrailResult"]["description"])

    # add routes (trails)
    for route in data["initialExploreMap"]["routes"]:
        for segment in route["lineSegments"]:
            line_points = polyline.decode(segment["polyline"]["pointsData"])
            height_points = polyline.decode(segment["polyline"]["indexedElevationData"])
            line = kml.newlinestring(
                # name="Route "+str(route["sequence_num"]),
                name=kml.document.name,
                coords=[        # combine x,y line with index,z line
                    (line_points[int(i*1000)][1], line_points[int(i*1000)][0], z)
                    for i,z in height_points
                ]
            )
            line.description = kml.document.description
            line.style.linestyle.color = "ff1a86eb"
            line.style.linestyle.width = 2.5

    # add waypoints
    for waypoint in data["initialExploreMap"]["waypoints"]:
        point = kml.newpoint(
            name=waypoint["name"],
            coords=[(waypoint["location"]["longitude"], waypoint["location"]["latitude"])]
        )
        if waypoint.get("description") is not None:
            point.description = waypoint["description"].strip()
        point.style.iconstyle.color = "ffeb891a"
        point.style.iconstyle.icon.href = "https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png"

    # write kml file
    kml.save(OUTPUT_PATH+data["initialExploreMap"]["name"]+".kml")


# if running this file directly
if __name__ == "__main__":
    # no args provided, run for all files
    if len(sys.argv) == 1:
        for file_name in os.listdir(EXTRACTED_PATH):
            data_json_to_kml(file_name)
    # assume all args are one file name, with spaces
    else:
        data_json_to_kml(" ".join(sys.argv[1:]))
