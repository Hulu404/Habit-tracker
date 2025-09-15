import json
from prettytable import PrettyTable

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


    if data:
        # Создаем таблицу, используя ключи первого элемента как заголовки
        table = PrettyTable(field_names=data[0].keys())
        for item in data:
            table.add_row(item.values())
        print(table)