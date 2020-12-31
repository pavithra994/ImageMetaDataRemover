from PIL import Image


import os
files = [f for f in os.listdir('.') if os.path.isfile(f) and not f.endswith(".py")]
files = sorted(files)
print(files)
for i, f in enumerate(files):
    print(f,type(f))
    try:
        formt = f.split(".")[-1]
        image = Image.open(f)

        # next 3 lines strip exif
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        image_without_exif.save("New folder/{}.{}".format(str(i).zfill(4),formt))
    except Exception as e:
        print(e)


