import lib
from PIL import Image, ImageDraw
import settings.settings as settings
import models.DataModel as DataModel
import models.ClientModel as ClientModel

def create_raport(token, db, DataClass, ClientClass):
    error = False
    data = DataModel.get_data(token, db, DataClass)
    proportion = ClientModel.get_proportion(token, db, ClientClass);
    if proportion == -1:
        error = True
    build_matrix(data, proportion)
    


def build_matrix(data, proportion):
    tab = []
    period = 0.1

    tmp_x_size = int(settings.MATRIX_WIDTH // (settings.MATRIX_WIDTH * period))
    tmp_y_size = int((int(settings.MATRIX_WIDTH * proportion) + 1) // (settings.MATRIX_WIDTH * period))

    for i in range(tmp_x_size):
        tab.append([])
        for j in range(tmp_y_size):
            tab[i].append(0)

    max_value = 1

    for i in data:
        tmp = settings.MATRIX_WIDTH * (i.x / 100)
        box_x = int(tmp // (settings.MATRIX_WIDTH * period))
        tmp = settings.MATRIX_WIDTH * proportion * (i.y / 100)
        box_y = int(tmp // (settings.MATRIX_WIDTH * period))

        tab[box_y][tmp_x_size - box_x] += 1
        max_value = max(max_value, tab[box_y][tmp_x_size - box_x])
    
    generate_image(tab, proportion, max_value)
    print("MAX: ", max_value)

def generate_image(tab, proportion, max_value):
    print(tab)
    width = int(settings.MATRIX_WIDTH)
    height = int(settings.MATRIX_WIDTH * proportion)
    square_size = int(width * 0.1)

    image = Image.new('RGBA', (width, height), (255, 255, 255, 255))

    image_draw = ImageDraw.Draw(image)

    tmpX = 0
    tmpY = 0
    for x in range(0, width, square_size):
        tmpY = 0
        for y in range(0, height, square_size):
            color = (255, 132, 0, int(250 * (tab[tmpX][tmpY] / max_value)))
            square_coords = [(x, y), (x + square_size, y + square_size)]
            image_draw.rectangle(square_coords, fill=color)
            tmpY += 1
        tmpX += 1

    image.save('output.png')