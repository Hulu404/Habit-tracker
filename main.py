from files.handlers import *
import os
import json
from pathlib import Path

def main():
    scales_dict = {}
    while True:
        comd = input(f"Enter the command:\n - 1 Add new scale\n - 2 update scale\n - 3 finish program\n")

        if comd == "1":
            scale(scales_dict)

        elif comd == "2":
            if os.listdir("files/scales_archive"):
                for i in os.listdir(Path("files/scales_archive")):
                    print(i)

                name = input("Enter the name of scale: ")
                if name + ".json" in os.listdir("files/scales_archive"):
                    file_way = Path("files/scales_archive/" + name + ".json")
                    with open(file_way, "r", encoding="utf-8", newline="") as file:
                        data = json.load(file)

                    lines = []
                    count = 0
                    k = 1
                    key_c = input("Enter name of skill which you have mastered: ")
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

                    data[key_c] = " ".join(lines)

                    with open(file_way, "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)


                else:
                    print("No such file on directory!")
            else:
                print("No such file! Let's make it!\n")
                scale(scales_dict)

        elif comd == "3": break


if __name__ == "__main__":
    main()