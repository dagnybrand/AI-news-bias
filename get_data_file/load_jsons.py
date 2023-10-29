import json
import os

json_directory = './jsons'

python_objects = []

for json_file in os.listdir(json_directory):
    with open(json_directory + '/' + json_file, "r") as f:
        python_objects.append(json.load(f))

with open("bias_data.json", "w") as f:
    json.dump(python_objects, f, indent=4)