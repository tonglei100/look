import torch
import torch.nn as nn
from torch.autograd import Variable
from look import dataset
from look.cnn_model import CNN
from look import setting
import numpy as np
from look import one_hot
from PIL import Image


def train(model_name='model.pkl'):
    cnn = CNN()
    cnn.train()
    print('init net')
    criterion = nn.MultiLabelSoftMarginLoss()
    optimizer = torch.optim.Adam(
        cnn.parameters(), lr=setting.TRAIN_LEARNING_RATE)

    # Train the Model
    train_dataloader = dataset.get_train_data_loader()
    for epoch in range(setting.TRAIN_NUM_EPOCHS):
        for i, (images, labels) in enumerate(train_dataloader):
            images = Variable(images)
            labels = Variable(labels.float())
            predict_labels = cnn(images)
            loss = criterion(predict_labels, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print('epoch: % -3s loss: %s' % (epoch, loss.item()))
    torch.save(cnn.state_dict(), setting.MODEL_PATH /
               model_name)  # current is model.pkl
    print('save last model')


def test(model_name='model.pkl'):
    cnn = CNN()
    cnn.eval()
    cnn.load_state_dict(torch.load(setting.MODEL_PATH / model_name))
    print('load cnn net.')

    test_dataloader = dataset.get_test_data_loader()

    correct = 0
    total = 0
    for i, (images, labels) in enumerate(test_dataloader):
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        chars = ''
        for i in range(setting.MAX_CAPTCHA):
            chars += setting.ALL_CHAR_SET[np.argmax(predict_label[0, i * setting.ALL_CHAR_SET_LEN: (
                i + 1) * setting.ALL_CHAR_SET_LEN].data.numpy())]

        predict_label = chars
        true_label = one_hot.decode(labels.numpy()[0])
        total += labels.size(0)

        if(predict_label == true_label):
            correct += 1
        else:
            print('Predict:' + predict_label)
            print('Real   :' + true_label)
        if(total % 200 == 0):
            print('Test Accuracy of the model on the %d test images: %f %%' %
                  (total, 100 * correct / total))
    print('Test Accuracy of the model on the %d test images: %f %%' %
          (total, 100 * correct / total))


def recognize(model_name='model.pk'):
    cnn = CNN()
    cnn.eval()
    cnn.load_state_dict(torch.load(setting.MODEL_PATH / model_name))
    # print(load cnn net.)

    captcha_dataloader = dataset.get_captcha_data_loader()
    code = ''
    images = {}
    for image, label in captcha_dataloader:
        images[label] = image
    images = [images[key] for key in sorted(images)]
    for image in images:
        vimage = Variable(image)
        predict_label = cnn(vimage)

        for i in range(setting.MAX_CAPTCHA):
            code += setting.ALL_CHAR_SET[np.argmax(predict_label[0, i * setting.ALL_CHAR_SET_LEN: (
                i + 1) * setting.ALL_CHAR_SET_LEN].data.numpy())]

    return code


if __name__ == '__main__':
    code = recognize()
    print(code)
