def conversion_to_rgb(image_data):
    image_data_converted = image_data.convert('RGB')
    return image_data_converted


def conversion_to_rgba(image_data):
    image_data_converted = image_data.convert('RGBA')
    return image_data_converted
