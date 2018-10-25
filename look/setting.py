from pathlib import Path

NUMBER = ['2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)
MAX_CAPTCHA = 1

# 图像大小
IMAGE_HEIGHT = 26
IMAGE_WIDTH = 15

# 切图参数，图片大小要一致
box = {}
box[0] = (9,3,24,30)
box[1] = (24,3,39,30)
box[2] = (39,3,54,30)
box[3] = (54,3,69,30)

LOOK_PATH = Path('.')
DATASET_PATH = LOOK_PATH / 'dataset'
MODEL_PATH = LOOK_PATH / 'model'                   # 模型目录
SOURCE_TRAIN_PATH = DATASET_PATH / 'source_train'  # 原始训练图集
SOURCE_TEST_PATH = DATASET_PATH / 'source_test'    # 原始测试图集
TRAIN_PATH = DATASET_PATH / 'train'                # 训练图集
TEST_PATH = DATASET_PATH / 'test'                  # 测试图集
CAPTCHA_PATH = DATASET_PATH / 'captcha'            # 验证码图片，可以为切图
DOWNLOAD_PATH = DATASET_PATH / 'download'          # 要识别的验证码存放目录


# Hyper Parameters
TRAIN_NUM_EPOCHS = 100
# TRAIN_BATCH_SIZE = 64
TRAIN_LEARNING_RATE = 0.001
