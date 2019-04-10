from PIL import Image
from math import ceil
from random import randint


inp = list(map(ord, [i for i in input("Text: ")]))

for _ in range(3-len(inp) % 3):
    inp.append(255)

size = ceil((len(inp)//3 + 1) ** (1/2))

img = Image.new('RGB',
                (size, size),
                (randint(0, 256), randint(0, 256), randint(0, 256)
                 ))
t = 0
for y in range(size):
    for x in range(size):
        color = tuple(inp[t*3:(t+1)*3])
        if color:
            img.putpixel((x, y), color)
        t += 1
img.save("tmp.bmp", "BMP")
