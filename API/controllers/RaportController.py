import lib
from PIL import Image, ImageDraw
import config.config as config
import models.DataModel as DataModel
import models.ClientModel as ClientModel

def create_raport(token, db, DataClass, ClientClass):
    error = False
    data = DataModel.get_data(token, db, DataClass)
    proportion = ClientModel.get_proportion(token, db, ClientClass);
    if proportion == -1:
        return -1
    return build_matrix(data, proportion)
    
def build_matrix(data, proportion):
    tab = []
    period = config.PERIOD

    tmp_x_size = int(config.MATRIX_WIDTH // (config.MATRIX_WIDTH * period))
    tmp_y_size = int((int(config.MATRIX_WIDTH * proportion) + 1) // (config.MATRIX_WIDTH * period))

    for i in range(tmp_y_size + 1):
        tab.append([])
        for j in range(tmp_x_size + 1):
            tab[i].append(0)

    max_value = 1

    for i in data:
        box_x = int(tmp_x_size * (i.x / 100))
        box_y = int(tmp_y_size * (i.y / 100))
        tab[box_y][box_x] += 1
        max_value = max(max_value, tab[box_y][box_x])

    return generate_image(tab, proportion, max_value, period)

def generate_image(tab, proportion, max_value, period):
    width = int(config.MATRIX_WIDTH)
    height = int(config.MATRIX_WIDTH * proportion)
    square_size = int(width * period)

    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    image_draw = ImageDraw.Draw(image)

    tmpX = 0
    tmpY = 0
    for x in range(0, width, square_size):
        tmpY = 0
        for y in range(0, height, square_size):
            color = (255, 132, 0, int(250 * (tab[tmpY][tmpX] / max_value)))
            square_coords = [(x, y), (x + square_size, y + square_size)]
            image_draw.rectangle(square_coords, fill=color)
            tmpY += 1
        tmpX += 1

    name = "outputs/" + str(lib.get_hash()) + ".png"
    image.save(name)
    return name