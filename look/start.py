import look.setting
import setting
look.setting = setting

from look.cut import cut_captcha, cut_train, cut_test
from look.captcha import recognize, train, test


# 把 **原始训练图集** 切图为单个字符的图集，保存到 **训练图集** 中，本示例默认已切图，重新切图需把 **训练图集** 目录下图片删除
# **原始训练图集** 目录为 setting.SOURCE_TRAIN_PATH 配置，默认是  dataset/source_train/
# **训练图集** 目录为 setting.TRAIN_PATH 配置，默认是  dataset/train/
# cut_train()

# 把 **原始测试图集** 切图为单个字符的图集，保存到 **测试图集** 中，本示例默认已切图，重新切图需把 **测试图集** 目录下图片删除
# **原始测试图集** 目录为 setting.SOURCE_TEST_PATH 配置，默认是  dataset/source_test/
# **测试图集** 为 setting.TEST_PATH 配置，默认是  dataset/test/
# cut_test()

# 对 **训练图集** 进行训练，本示例默认已提供训练模型，重新训练前，需要删除 model.pkl 文件，或修改文件名
# model.pkl 是要保存的模型名称，可根据需要定义不同的名称
# model.pkl 存放目录为 setting.MODEL_PATH 配置，默认是 model/ 目录
# train('model.pkl')

# test，检验模型成功率，检测的是 **测试图集**
# test('model.pkl')

# 需要识别的验证码文件路径，可以为任意路径，默认为 setting.DOWNLOAD_PATH 配置，验证码名称可以为任意取名
picture = setting.DOWNLOAD_PATH / '5U62_1539929795.png'

# 如果训练的是切图后的图片集（如本示例），那么识别也需要切图，切图后图片放在 **验证码目录** 中
# **验证码目录** 目录为 setting.CAPTCHA_PATH 配置，默认是 dataset/captcha/
cut_captcha(picture)

# 识别 **验证码目录** 中的图片，如果为切图（即有多张图片，如本示例），会自动组合为字符串
# model.pkl 是要使用模型名称，请确保 setting.MODEL_PATH 配置的目录下有该文件
code = recognize('model.pkl')
print(code)
