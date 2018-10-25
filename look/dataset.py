from pathlib import Path
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from PIL import Image
from look import one_hot as ohe
from look import setting


class mydataset(Dataset):

    def __init__(self, folder, transform=None, flag=True):
        path = Path(folder)
        self.image_files = [f for f in path.iterdir()]
        self.transform = transform
        self.flag = flag  # 训练标记，为 False 时，是预测标记

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        image_root = self.image_files[idx]
        image_name = image_root.name
        image = Image.open(image_root)
        if self.transform is not None:
            image = self.transform(image)
        if self.flag:
            label = ohe.encode(image_name.split('_')[0])
        else:
            label = image_name.split('_')[0]
        return image, label


transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.ToTensor(),
])


def get_train_data_loader():
    dataset = mydataset(setting.TRAIN_PATH, transform=transform)
    return DataLoader(dataset, batch_size=64, shuffle=True)


def get_test_data_loader():
    dataset = mydataset(setting.TEST_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)


def get_predict_data_loader():
    dataset = mydataset(setting.PREDICT_PATH, transform=transform, flag=False)
    return DataLoader(dataset, batch_size=1, shuffle=True)


def get_captcha_data_loader(flodler=setting.CAPTCHA_PATH):
    dataset = mydataset(flodler, transform=transform, flag=False)
    return DataLoader(dataset, batch_size=1, shuffle=True)
