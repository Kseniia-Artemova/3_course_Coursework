import json


def open_json(path):
    with open(path, "rt", encoding="utf-8") as json_file:
        payments = json.load(json_file)
    return payments


for i in open_json("../sources/operations.json"):
    print(i)