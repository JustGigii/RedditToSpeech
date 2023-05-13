import json
import os


def addNewVideos(jsonarry: list):
    background_dir = "backgroundVideo"
    for subdir, dirs, files in os.walk(background_dir):
        for file in files:
            dir_path = os.path.join(subdir, file)
            newjson = {
                "name": file,
                "path": dir_path,
                "isfhnish": False,
                "currentTime": 0,
            }
            if len(jsonarry) == 0:
                jsonarry.append(newjson)
            else:
                for json in jsonarry:
                    if file != json["name"]:
                        jsonarry.append(newjson)


def InitJson():
    json_data = []
    # If file exists, open it and read the JSON data
    with open("video.json", "r") as f:
        data = f.read()
        # Check if the file is empty or contains invalid JSON
        if len(data) == 0:
            # If file is empty, create a new empty JSON object and write it to the file
            addNewVideos(json_data)
            with open("video.json", "w") as f:
                json.dump(json_data, f)
            print("Created new video.json file with empty JSON object.")
        else:
            # If file contains valid JSON, load it and display all objects in the file
            print("JSON objects in video.json:")
            json_data = json.loads(data)
            addNewVideos(json_data)
        f.close()
    return json_data


def updatefile(jsonarry):
    # Open the video.json file for reading and writing
    with open("video.json", "w") as f:
        # Set the file pointer to the beginning of the file and truncate the file
        json.dump(jsonarry, f)
        f.close()


def loadvideo(json_data):
    index = 0
    while json_data[index]["isfhnish"] == True and index < len(json_data):
        index += 1
    if index < len(json_data):
        return index
    return -1


# json_data = InitJson()
# print(json_data[0])
# json_data[0]["currentTime"] = 9
# # print(json_data)
# updatefile(json_data)
# print(loadvideo())
