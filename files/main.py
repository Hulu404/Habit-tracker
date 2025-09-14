from handlers import *

def main():

    scales_dict = {}

    while True:

        comd = input(f"Enter the command:\n - 1 Add new scale\n - 2 show all scales\n - 3 add XP in scale\n - 4 finish the program\n ")

        if comd == "1":

            text = input("Enter the name of scale: ")
            scale_name = text
            text = list()

            scales_dict[scale_name] = text
            # Тут можно задать запись в json файл, чтобы сохранить отдельный список для каждого пользователя

            show_scale_table(scales_dict)

        elif comd == "2":
            show_scale_table(scales_dict)

        elif comd == "3":

            if len(scales_dict) == 0:
                print("Dictinary is empty!")
            else:
                show_scale_table(scales_dict)

                choose = input("Enter the scale name: ")

                scales_dict[choose].append(25)
                show_scale_table(scales_dict)

        elif comd == "4":
            show_scale_table(scales_dict)
            break


if __name__ == "__main__":
    main()