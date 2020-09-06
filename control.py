from pathlib import Path

from PIL import Image

from Conversions import colorModels


class Picture:
    def __init__(self, path_folder, filename):
        self.path_folder = path_folder
        filename_details = filename.split('.')
        self.filename_original = ''.join(filename_details[0:-1])
        self.filetype_original = filename_details[-1]
        self.image_original = Image.open(
            (self.path_folder / (self.filename_original + '.' + self.filetype_original)),
            'r'
        )
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

    def save_image(self, file_type):
        file_type_list = [
            'jpg', 'JPG', 'jpeg', 'JPEG', 'bmp', 'BMP', 'png', 'PNG'
        ]
        if file_type in file_type_list:
            self.image_converted.save(
                self.path_folder.parent / 'Output' / (self.filename_original + '.' + file_type)
            )
        else:
            print('File type is not supported.')


if __name__ == '__main__':
    folder_path = Path('Input')
    folder_path_content = folder_path.glob('**/*')
    files = [file.name for file in folder_path_content if file.is_file()]
    pictures = [
        Picture(
            path_folder=folder_path,
            filename=file
        ) for file in files
    ]
