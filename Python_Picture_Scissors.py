
# Author: Dodson
# Name: Python_Picture_Scissors 1024*1024
# %%
from PIL import Image


def image_magic(image, name=''):

    # 切割圖片
    width, height = image.size
    new_width = width // 2
    new_height = height // 2

    # 切割左上角
    left_upper = image.crop((0, 0, new_width, new_height))
    left_upper.save(name + '_left_upper.png')

    # 切割右上角
    right_upper = image.crop((new_width, 0, width, new_height))
    right_upper.save(name + '_right_upper.png')

    # 切割左下角
    left_lower = image.crop((0, new_height, new_width, height))
    left_lower.save(name + '_left_lower.png')

    # 切割右下角
    right_lower = image.crop((new_width, new_height, width, height))
    right_lower.save(name + '_right_lower.png')


# %%
# 載入圖片
image = Image.open(
    'capture_the_decadent_beauty_of_a_sophisticated_chocolate_1e6d9f30-f309-4ecd-939f-c17d51014476.png')

image_magic(image, name='chocolate_cake')

# %%
