
import time
from PIL import Image
from pathlib import Path
from look import setting


def cut_image(f, box, target_folder='dataset/test', t=int(time.time())):
    f = Path(f)
    image=Image.open(f)

    for k in box:
        im = image.crop(box[k])
        char = f.name[k]
        name = char + '_' + str(t) + '.png'
        t += 1
        im.save(Path(target_folder) / name,'PNG')


def cut_captcha(f, box=setting.box, target_folder=setting.CAPTCHA_PATH):
    f = Path(f)
    image=Image.open(f)

    i = 1
    for k in box:
        im = image.crop(box[k])
        name = str(i) + '.png'
        i += 1
        im.save(Path(target_folder) / name,'PNG')


def cut_images(box, source_folder, target_folder):
    t = int(time.time())

    source_path = Path(source_folder)
    all_images = []
    for f in source_path.iterdir():
        t += len(box)
        cut_image(f, box, target_folder, t)


def cut_train(box=setting.box, source_folder='dataset/source_train', target_folder='dataset/train'):
    cut_images(box, source_folder, target_folder)


def cut_test(box=setting.box, source_folder='dataset/source_test', target_folder='dataset/test'):
    cut_images(box, source_folder, target_folder)


if __name__=='__main__':
    box = {}
    box[0] = (9,3,24,30)
    box[1] = (24,3,39,30)
    box[2] = (39,3,54,30)
    box[3] = (54,3,69,30)

    cut_train(box)
