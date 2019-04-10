from PIL import Image

img = Image.open('tmp.bmp')

for y in range(img.size[1]):
    for x in range(img.size[0]):
        p = img.getpixel((x, y))
        for j in p:
            print(chr(j), end='')
