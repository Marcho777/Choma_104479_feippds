""" Tento modul implementuje konvertovanie RGB obrázka do grayscale.
Implemetácia využíva 2 riešenia jedno s použitím GPU a druhé s použitím CPU.
"""

__authors__ = "Marián Choma, Tomáš Vavro"
__email__ = "xchoma@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"

import numpy as np
from PIL import Image
from numba import cuda
import os
import time


@cuda.jit
def rgb2gray_kernel(rgb_array, gray_array):
    """ CUDA kernel funkcia pre konvertovanie RGB obrázka do grayscale

    :param rgb_array: pole reprezentujúce rgb obrázok
    :param gray_array: pole reprezentujúce grayscale obrázok
    :return:
    """
    x, y = cuda.grid(2)
    if x < rgb_array.shape[0] and y < rgb_array.shape[1]:
        r = rgb_array[x, y, 0]
        g = rgb_array[x, y, 1]
        b = rgb_array[x, y, 2]
        gray_array[x, y] = 0.2989 * r + 0.5870 * g + 0.1140 * b


def cpu_convert():
    """ Funkcia ktorá konvertuje RGB obrázok do grayscale s použitím CPU

    :return:
    """
    directory = './images/'
    index = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            index += 1
            image = Image.open(f)
            gray_image = Image.new("L", image.size)
            for x in range(image.width):
                for y in range(image.height):
                    r, g, b = image.getpixel((x, y))
                    gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
                    gray_image.putpixel((x, y), gray)

            gray_image.save(f"./grayscale/gray_image{index}.jpg")


def gpu_convert():
    """ Funkcia ktorá konvertuje RGB obrázok do grayscale s použitím GPU

    :return:
    """
    directory = './images/'
    index = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            index += 1
            image = Image.open(f)
            rgb_array = np.array(image)
            gray_array = np.empty(shape=(rgb_array.shape[0], rgb_array.shape[1]), dtype=np.float32)

            threads_per_block = (16, 16)
            blocks_per_grid_x = (rgb_array.shape[0] + threads_per_block[0] - 1) // threads_per_block[0]
            blocks_per_grid_y = (rgb_array.shape[1] + threads_per_block[1] - 1) // threads_per_block[1]
            blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)
            rgb2gray_kernel[blocks_per_grid, threads_per_block](rgb_array, gray_array)

            gray_image = Image.fromarray(gray_array.astype(np.uint8))
            gray_image.save(f"./grayscale/gray_image{index}.jpg")


if __name__ == "__main__":
    start = time.time()
    gpu_convert()
    cpu_convert()
    end = time.time()
    print(end - start)
