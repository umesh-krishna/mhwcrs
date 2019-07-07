from PIL import Image
import numpy as np
import os
import platform


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])


def load_image(file_name):
    img = Image.open(file_name)
    img.convert("1")
    # img.load()

    data = np.asarray(img, dtype="int32")
    return rgb2gray(data)


def save_image(npdata, out_file_name):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"), "L")
    img.save(out_file_name)


def show_image_array(npdata):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"), "L")
    img.save('temp-0001.jpg')
    show_image('temp-0001.jpg')


def show_image(img1):
    if platform.system() == 'Windows':
        os.system("powershell -c "+img1)
    elif platform.system() == 'Linux':
        os.system("xdg-open "+img1)

