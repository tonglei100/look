import look.setting
import setting
look.setting = setting

from look.cut import cut_captcha, cut_train, cut_test
from look.captcha import recognize, train, test


# 把训练图集切图为单个字符的图集，默认已切图，重新切图需把 dataset/train 目录下图片删除
# cut_train()

# test 切图，默认已切图，重新切图需把 dataset/test 目录下图片删除
# cut_test()

# train，默认已提供训练模型，重新训练前，需要删除 model.pkl 文件
# train('model.pkl')

# test，检验模型成功率
# test('model.pkl')


captcha_path = setting.DOWNLOAD_PATH / '5U62_1539929795.png'

# 如果需要切图
cut_captcha(captcha_path)

# 默认是识别 dataset/captcha 目录，如果为切图，会自动组合为字符串
code = recognize('model.pkl')
print(code)
