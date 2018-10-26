import look.setting
import setting
look.setting = setting

from look.cut import cut_captcha, cut_train, cut_test
from look.captcha import recognize, train, test


# 把训练图集切图为单个字符的图集，本示例默认已切图，重新切图需把 **训练图集** 目录下图片删除
# 训练图集存放路径为 setting.TRAIN_PATH 配置，默认是  dataset/train
# cut_train()

# test 切图，本示例默认已切图，重新切图需把 **测试图集** 目录下图片删除
# 测试图集存放路径为 setting.TEST_PATH 配置，默认是  dataset/test
# cut_test()

# train，本示例默认已提供训练模型，重新训练前，需要删除 model.pkl 文件
# model.pkl 存放目录为 setting.MODEL_PATH 配置，默认是 model 目录
# train('model.pkl')

# test，检验模型成功率，检测的是测试图集目录
# test('model.pkl')

# 需要失败的验证码文件路径，验证码名称可以为任意取名
captcha_path = setting.DOWNLOAD_PATH / '5U62_1539929795.png'

# 如果训练的是切图后的图片，那么识别也需要切图。本示例中，提供的是以切图训练后的模型
cut_captcha(captcha_path)

# 识别验证码目录的图片，如果为切图（即有多张图片），会自动组合为字符串
# 验证码目录为 setting.CAPTCHA_PATH 配置，默认是 dataset/captcha 目录
code = recognize('model.pkl')
print(code)
