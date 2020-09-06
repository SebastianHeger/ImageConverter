def conversion_to_rgb(image_data):
    image_data_converted = image_data.convert('RGB')
    return image_data_converted


def conversion_to_rgba(image_data):
    image_data_converted = image_data.convert('RGBA')
    return image_data_converted


def conversion_to_cmyk(image_data):
    image_data_converted = image_data.convert('CMYK')
    return image_data_converted


def conversion_to_hsv(image_data):
    image_data_converted = image_data.convert('HSV')
    return image_data_converted


def conversion_to_lab(image_data):
    image_data_converted = image_data.convert('LAB')
    return image_data_converted
