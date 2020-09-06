from pathlib import Path

from PIL import Image

from Conversions import colorModels


class Picture:
    def __init__(self, path):
        self.image_original = Image.open(path, 'r')
        # self.width_original, self.height_original = self.image_original.size
        self.image_converted = None

    def color_conversion(self, model_type):
        if model_type == 'RGB' or model_type == 'rgb':
            self.image_converted = colorModels.conversion_to_rgb(self.image_original)
        elif model_type == 'RGBA' or model_type == 'rgba':
            self.image_converted = colorModels.conversion_to_rgba(self.image_original)
        elif model_type == 'CMYK' or model_type == 'cmyk':
            self.image_converted = colorModels.conversion_to_rgba(self.image_original)
        elif model_type == 'HSV' or model_type == 'hsv':
            self.image_converted = colorModels.conversion_to_rgba(self.image_original)
        elif model_type == 'LAB' or model_type == 'lab':
            self.image_converted = colorModels.conversion_to_rgba(self.image_original)


if __name__ == '__main__':
    file_path = Path('Input')
    file_path_content = file_path.glob('**/*')
    files = [file for file in file_path_content if file.is_file()]
    pictures = [Picture(path=file) for file in files]
