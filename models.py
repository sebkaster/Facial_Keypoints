import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel

        # output size = ((W-F)/S +1) / MaxPoolFilter
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.conv2 = nn.Conv2d(32, 64, 4)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv4 = nn.Conv2d(128, 256, 2)


        self.max_pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(p=0.1)

        # 256 outputs * the 12*12 filtered/pooled map size = 36864
        self.fc1 = nn.Linear(256 * 12 * 12, 1000)

        ## last layer output has 136 values, 2 for each of the 68 keypoint (x, y) pairs
        self.fc3 = nn.Linear(1000, 136)

    def forward(self, x):
        x = self.max_pool(F.relu(self.conv1(x)))
        x = self.dropout(x)
        x = self.max_pool(F.relu(self.conv2(x)))
        x = self.dropout(x)
        x = self.max_pool(F.relu(self.conv3(x)))
        x = self.dropout(x)
        x = self.max_pool(F.relu(self.conv4(x)))
        x = self.dropout(x)

        # Flatten feature maps into a vector
        x = x.view(x.size(0), -1)

        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc3(x)

        # a modified x, having gone through all the layers of your model
        return x