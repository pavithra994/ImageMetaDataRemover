from PIL import Image
import os
from time import sleep


FOLDER_NAME = "Images"

def delete_file(file_list:[],initial_print_lines=""):
    for i,file in enumerate(file_list):
        y = i+1
        x = len(file_list) - y
        p = (y/len(file_list))*100 if y != 0 else 0
        os.system('cls')
        print(initial_print_lines)
        print("Deleting old files... {}{} : {:.2f}%".format("|"*y,"="*x,p))
        os.remove(file)
        sleep(1)

    os.system('cls')
    print(initial_print_lines)
    print("Total {} files are deleted".format(len(file_list)))



files = [f for f in os.listdir('.') if os.path.isfile(f) and not f.lower().endswith(".py")]
files = sorted(files)

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

completed_files = []
error_files = []

for i, f in enumerate(files):

    print("Meta data cleaning... : {}/{}".format(i+1,len(files)))
    try:
        formt = f.split(".")[-1]
        image = Image.open(f)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save("{}/{}.{}".format(FOLDER_NAME,str(i).zfill(4),formt))
        completed_files.append(f)
    except Exception as e:
        error_files.append({"file":f, "error":e})

    os.system('cls')

print("Completed ----- {}/{}".format(len(completed_files),len(files)))

delete_file(completed_files,"Completed ----- {}/{}".format(len(completed_files),len(files)))

if len(completed_files) == len(files):
    print("All operations are done....")
    sleep(2)
else:
    print("Errors occur in following files : ")
    for ef in error_files:
        print("{} : {} ".format(ef["file"],ef["error"]))

    x = input("press any key to close...")
