from PIL import Image

img = Image.open(input("Image: "))  # Считывание картинки

# Получаем координаты из первого пикселя и выводим букву, которая в нем хранится
x = img.getpixel((0, 0))[0]
y = img.getpixel((0, 0))[1]
print(chr(img.getpixel((0, 0))[2]), end='')

while img.getpixel((x, y))[2] != 0:
    print(chr(img.getpixel((x, y))[2]), end='')
    xOld, yOld = x, y
    x = img.getpixel((xOld, yOld))[0]
    y = img.getpixel((xOld, yOld))[1]
