import math
from PIL import Image, ImageDraw


def calc_color_dist(data_source, data_compare):
    distances = list()
    for index, pixel_source in enumerate(data_source):
        pixel_compare = data_compare[index]
        distances.append(abs(pixel_source-pixel_compare))
    distance = math.sqrt(sum([i ** 2 for i in distances]))
    return distance


def color_remover(image_data, image_data_type, color_remove, color_insert, distance):
    image_data_edit = image_data
    width, height = image_data.size
    for step_x in range(width):
        for step_y in range(height):
            pixel_data = image_data.getpixel((step_x, step_y))
            if image_data_type == 'RGB' or image_data_type == 'rgb':
                if calc_color_dist(
                        data_source=pixel_data,
                        data_compare=color_remove
                ) > distance:
                    image_data_edit.putpixel((step_x, step_y), color_insert)
    return image_data_edit
