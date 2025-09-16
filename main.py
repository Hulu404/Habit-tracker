import os
import json
from pathlib import Path


def main():

    scales_dict = {}
    file_path = None

    while True:
        comd = input(f"Enter the command:\n - 1 Add new scale\n - 2 update scale\n - 3 finish program")

        if comd == "1":

            scale_name = input("Enter the name of scale: ")

            if scales_dict in os.listdir(file_path): # Проверка существования файла
                print(f"Scale {scale_name} already exists!")

            else:    # В случае, если файла не сущетсвует, то он будет создаваться
                file_path = Path(f"scales_archive/{scale_name}.json")
                days = int(input("Enter the days: "))
                scales_dict[scale_name] = {}
                scales_dict[scale_name]["days"] = days

                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(scales_dict, file, ensure_ascii=False, indent=4)

                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)



        elif comd == "2":
            print(os.listdir("scales_archive"), sep="\n")

            name = input("Enter the name of scale: ")

            if name + ".json" in os.listdir("scales_archive"):
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

                file_path = Path("scales_archive/" + name + ".json")
                dict_scales[name] = lines
                scales_dict[name] = dict_scales
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(scales_dict, file, ensure_ascii=False, indent=4)

                with open(file_path, "r", encoding="utf-8", newline="") as file:
                    data = json.load(file)

                print(data)

            else:
                print("No!")

        elif comd == "3": break


if __name__ == "__main__":
    main()