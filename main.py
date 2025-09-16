import os
import json
from pathlib import Path
from files.handlers import *


def main():

    scales_dict = {}
    file_path = None

    while True:
        comd = input(f"Enter the command:\n - 1 Add new scale\n - 2 update scale\n - 3 finish program\n")

        if comd == "1":
            scale(scales_dict)

        elif comd == "2":
            for _ in os.listdir("files/scales_archive"):
                print(_)

            name = input("Enter the name of scale: ")

            if name + ".json" in os.listdir("files/scales_archive"):
                lines = []
                count = 0
                k = 1
                dict_scales = {name: []}
                print("Enter the text: ")
                while True:
                    line = input(f"{k}| ")
                    k += 1

                    if line:
                        lines.append(line)
                    else:
                        count += 1

                    if count == 2: break
                    else: continue

                file_path = Path("files/scales_archive" + name + ".json")
                dict_scales[name] = lines
                scales_dict[name] = dict_scales
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(scales_dict, file, ensure_ascii=False, indent=4)

                with open(file_path, "r", encoding="utf-8", newline="") as file:
                    data = json.load(file)

                print(data)

            else:
                pass

        elif comd == "3": break


if __name__ == "__main__":
    main()