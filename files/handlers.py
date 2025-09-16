import json
import os
from pathlib import Path

def show_scale_table(dictionary):
    for _ in dictionary.keys():
        print(f"{_} - {dictionary[_]}")


def make_json_file(dictionary):
    with open("scales_archive/Scales.json", "w", encoding="utf-8", newline="") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)

    with open("scales_archive/scales.json", "r", encoding="utf-8", newline="") as file:
        data = json.load(file)

    return data

def show(scale_name):
    file_path = Path("files/scales_archive" + scale_name + ".json")
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        data = json.load(file)


def scale(scales_dict):
    scale_name = input("Enter the name of scale: ")
    file_path = Path("files/scales_archive" + scale_name + ".json")

    if scales_dict in os.listdir(file_path):  # Проверка существования файла
        print(f"Scale {scale_name} already exists!")

    else:  # В случае, если файла не сущетсвует, то он будет создаваться
        file_path = Path(f"scales_archive/{scale_name}.json")
        days = int(input("Enter the days: "))
        scales_dict[scale_name] = {}
        scales_dict[scale_name]["days"] = days

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(scales_dict, file, ensure_ascii=False, indent=4)

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    return data