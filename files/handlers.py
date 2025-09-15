import json

def show_scale_table(dictionary):
    for _ in dictionary.keys():
        print(f"{_} - {dictionary[_]}")


def make_json_file(dictionary):
    with open("scales_archive/Scales.json", "w", encoding="utf-8", newline="") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)

    with open("scales_archive/scales.json", "r", encoding="utf-8", newline="") as file:
        data = json.load(file)

    return data

def show():
    with open("scales_archive/scales.json", "r", encoding="utf-8", newline="") as file:
        data = json.load(file)

