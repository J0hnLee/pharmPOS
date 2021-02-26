import os
import torch
import numpy as np
import random

from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms


class Data(Dataset):
    def __init__(self, data_root, transforms_=None, mode='train'):
        if mode == 'train':
            self.transform = transforms_
        else:
            self.transform = transforms.Compose([
                transforms.Resize(size=(30, 30)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[.5], std=[.4])
            ])
        self.image_names = []
        for root, sub_filder, file_list in os.walk(os.path.join(data_root, mode)):
            self.image_names += [os.path.join(root, file_path) for file_path in file_list]

        random.shuffle(self.image_names)
        self.labels = [int(file_name[len(data_root):].split('/')[2]) for file_name in self.image_names]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        image = self.transform(Image.open(self.image_names[idx]))
        # image = Image.open(self.image_names[idx])
        label = torch.tensor(self.labels[idx])

        return {'X': image, 'Y': label}


class TestData(Dataset):
    def __init__(self, data):
        self.transform = transform = transforms.Compose([
            transforms.Resize(size=(30, 30)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[.5], std=[.4])
        ])
        self.input = data

    def __len__(self):
        return len(self.input)

    def __getitem__(self, idx):
        img = self.transform(Image.fromarray(self.input[idx]))

        return img
