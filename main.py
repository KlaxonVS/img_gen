import os
from datetime import datetime as dt
import random
from PIL import Image

from rgb_colors_list import RGB_NAMES

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SAMPLES_DIR = os.path.join(BASE_DIR + '\img_samples')

RESULT_IMGS = os.path.join(BASE_DIR + '\generated_img')

if not os.path.isdir(RESULT_IMGS):
    os.mkdir(RESULT_IMGS)

SAMPLES_LIST = os.listdir(SAMPLES_DIR)

COORDINATES = {0: [100, 700], 1: [700, 100], 2: [1300, 700], 3: [700, 1300]}

WIDTH = 6000
HEIGHT = 6000

BRICK_WIDTH = 2000
BRICK_HEIGHT = 2000

UNIQ_IMG_DICT = {}


def uniq_img_compile():
    random_img_file = random.choice(SAMPLES_LIST)
    i = 0
    while len(UNIQ_IMG_DICT) < 4:
        if random_img_file not in UNIQ_IMG_DICT.values():
            UNIQ_IMG_DICT[i] = random_img_file
            i += 1
        random_img_file = random.choice(SAMPLES_LIST)
    return UNIQ_IMG_DICT


def main():
    brick_img = Image.new(
        mode='RGB', size=(BRICK_WIDTH, BRICK_HEIGHT),
        color=random.choice(RGB_NAMES)
    )
    uniq_img_compile()
    for i, sample_img in UNIQ_IMG_DICT.items():
        sample_img = Image.open(SAMPLES_DIR + f'\{sample_img}')
        brick_img.paste(sample_img, COORDINATES[i], mask=sample_img)
        sample_img.close()
    background = Image.new('RGB', (WIDTH, HEIGHT))
    background.paste(brick_img, (0, 0,))
    background.paste(brick_img, (0, BRICK_HEIGHT,))
    background.paste(brick_img, (0, BRICK_HEIGHT * 2,))
    background.paste(brick_img, (BRICK_WIDTH, 0,))
    background.paste(brick_img, (BRICK_WIDTH, BRICK_HEIGHT,))
    background.paste(brick_img, (BRICK_WIDTH, BRICK_HEIGHT * 2,))
    background.paste(brick_img, (BRICK_WIDTH * 2, 0,))
    background.paste(brick_img, (BRICK_WIDTH * 2, BRICK_HEIGHT,))
    background.paste(brick_img, (BRICK_WIDTH * 2, BRICK_HEIGHT * 2,))
    now = dt.now()
    date = now.strftime('%d%m%y-%H%M%S')
    name = '\{name}-{date}.jpeg'.format(name='img', date=date,)
    background.save(RESULT_IMGS + name,)
    result = Image.open(RESULT_IMGS + name,)
    result.show()


if __name__ == '__main__':
    main()
