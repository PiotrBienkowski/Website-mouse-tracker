from PIL import Image, ImageDraw
import random

width = 500
height = 500
square_size = width // 10
num_squares = (width * height) // (square_size ** 2)

image = Image.new('RGBA', (width, height), (255, 255, 255, 255))

image_draw = ImageDraw.Draw(image)

for x in range(0, width, square_size):
    for y in range(0, height, square_size):
        color = (255, 132, 0, random.randint(0, 255))
        square_coords = [(x, y), (x + square_size, y + square_size)]
        image_draw.rectangle(square_coords, fill=color)

image.save('output.png')