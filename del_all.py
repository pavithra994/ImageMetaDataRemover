import os
from time import sleep


def delete_file(file_list:[],initial_print_lines="",waiting=1):
    for i,file in enumerate(file_list):

        y = i+1
        x = len(file_list) - y
        p = (y/len(file_list))*100 if y != 0 else 0
        os.system('cls')
        if initial_print_lines == "":
            is_image = "AN IMAGE" if f.lower().endswith(".jpg") or f.lower().endswith(
                ".png") else "WARNING: NOT AN IMAGE"
            print("Now deleting: - {} | {}".format(file,is_image))
        else:
            print(initial_print_lines)
        print("Deleting old files... {}{} : {:.2f}%".format("|"*y,"="*x,p))
        sleep(waiting)
        os.remove(file)

    os.system('cls')
    print(initial_print_lines)
    print("Total {} files are deleted".format(len(file_list)))



files = [f for f in os.listdir('.') if os.path.isfile(f) and not f.lower().endswith(".py")]
files = sorted(files)
print("Are sure to delete following files: ")
for f in files:
    is_image = "AN IMAGE" if f.lower().endswith(".jpg") or f.lower().endswith(".png") else "WARNING: NOT AN IMAGE"
    print("{} : {}".format(f,is_image))

input_par = input("Are you sure to continue this deleting process? (Y/N)")

if input_par.lower() == "y":
    delete_file(files)
    w = input("Press Enter to exit...")
else:
    pass