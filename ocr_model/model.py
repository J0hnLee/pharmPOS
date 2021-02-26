import torch.nn as nn
import torch.nn.functional as F

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 64, 3, padding=3//2)
        self.conv2 = nn.Conv2d(64, 128, 3, padding=3//2)
        self.conv3 = nn.Conv2d(128, 256, 3, padding=3//2)
        self.conv4 = nn.Conv2d(256, 512, 3, padding=3//2)
        self.conv5 = nn.Conv2d(512, 512, 3, padding=3//2)
        self.pool = nn.MaxPool2d(2, padding=2//2)

        self.fc = nn.Sequential(
            nn.Linear(512*3*3, 1024),
            nn.ReLU(inplace=True),
            nn.Linear(1024, 403)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.pool(x)
        x = self.conv3(x)
        x = self.pool(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x