import numpy as np
from PIL import Image
from numba import cuda
import os
import time


@cuda.jit
def rgb2gray_kernel(rgb_array, gray_array):
    x, y = cuda.grid(2)
    if x < rgb_array.shape[0] and y < rgb_array.shape[1]:
        R = rgb_array[x, y, 0]
        G = rgb_array[x, y, 1]
        B = rgb_array[x, y, 2]
        gray_array[x, y] = 0.2989 * R + 0.5870 * G + 0.1140 * B


def cpu_convert():
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
    directory = './images/'
    index = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            index += 1
            image = Image.open(f)
            rgb_array = np.array(image)

            # Allocate memory for output array
            gray_array = np.empty(shape=(rgb_array.shape[0], rgb_array.shape[1]), dtype=np.float32)

            # Configure kernel and launch
            threads_per_block = (16, 16)
            blocks_per_grid_x = (rgb_array.shape[0] + threads_per_block[0] - 1) // threads_per_block[0]
            blocks_per_grid_y = (rgb_array.shape[1] + threads_per_block[1] - 1) // threads_per_block[1]
            blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)
            rgb2gray_kernel[blocks_per_grid, threads_per_block](rgb_array, gray_array)

            # Convert output array to image and save
            gray_image = Image.fromarray(gray_array.astype(np.uint8))
            gray_image.save(f"./grayscale/gray_image{index}.jpg")


if __name__ == "__main__":
    start = time.time()
    gpu_convert()
    cpu_convert()
    end = time.time()
    print(end - start)
