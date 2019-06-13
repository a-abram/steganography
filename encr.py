from PIL import Image
from math import ceil
from random import randint


inp = list(map(ord, [i for i in input("Text: ")]))  # Чтение текста из сконсоли
image = Image.open(input("Image: "))  # Считывание картинки
inp.append(0)  # чтобы было понятно, когда заканчивается текст. Аналог \0

width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту

# Записываем в самый первый пиксель координаты следующего
x = randint(1, width)
y = randint(1, height)
image.putpixel((0, 0), (x, y, inp[0]))
inp.remove(inp[0])

busy = []
for num in inp:
    xOld, yOld = x, y
    x = randint(1, width-1)  # Генерируем случайные координаты
    y = randint(1, height-1)
    while (x, y) in busy:  # Если эти координаты заняты, создаем новые
        x = randint(1, width-1)
        y = randint(1, height-1)
    image.putpixel((xOld, yOld), (x, y, num))  # Записываем в картинку
    busy.append((x, y))  # Запоминаем, что мы в них что-то записали

image.save("tmp.bmp", "BMP")
