![Look](https://github.com/tonglei100/look/blob/master/snapshot/logo.jpg?raw=true)

# Look

Look 是一款基于 CNN 训练的验证码识别工具，提供切图、训练、测试、识别等方法，优点是样本需求少，运行速度快，使用超级简单。


## 安装

### 前提条件

#### PyTorch 安装

访问 https://pytorch.org/get-started/locally/

找到适合自己的安装方式，如 Python3.6 的安装方式：

```
# Python 3.6
pip3 install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-win_amd64.whl
pip3 install torchvision
```


### look 安装

#### 初次安装

    pip install look

#### 升级

    pip install -U look


## 快速体验

在合适的目录，如 D:\\ 目录下，打开 CMD 命令行窗口，输入如下命令

```shell
look
cd look_example
python start.py
```

# 后记

本项目是基于开源项目 [pytorch-captcha-recognition](https://github.com/dee1024/pytorch-captcha-recognition)，主要做了以下功能优化：

1. train 中加入 cnn.train()
2. recognize 中加入 cnn.eval()
3. 增加切图处理，大大减少了训练集样本数量
4. one_hot 函数优化
5. 函数接口简化
6. 提供 pip 安装包
7. 提供示例

最后，感谢 Dee Qiu @dee1024 的贡献。
