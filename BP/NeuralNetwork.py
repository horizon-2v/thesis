import torch
import torch.nn.functional as F
import os
import pandas as pd
from torch.utils.data import Dataset
from torch.utils.data.dataset import T_co
from torch.utils.data import DataLoader
from torch import nn


def input_transform(input):
    data = torch.as_tensor(input).T.float()
    return data


class CustomImageDataset(Dataset):
    def __init__(self, annotation_file, data_dir, transform=input_transform, target_transform=None):
        self.labels = pd.read_csv(annotation_file, usecols=[1, 2])
        self.dir = data_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index) -> T_co:
        data_path = os.path.join(self.dir, self.labels.iloc[index, 0])
        data = pd.read_csv(data_path, usecols=[1, 2, 3]).values
        label = self.labels.iloc[index, 1]
        if self.transform:
            data = self.transform(data)
        if self.target_transform:
            label = self.target_transform(label)
        return data, label


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.GRU = nn.GRU(input_size=1001, hidden_size=10, num_layers=2, batch_first=True)
        self.GRU_relu_stack = nn.Sequential(
            # nn.Linear(3*1001, 512),
            nn.ReLU(),
            nn.Linear(20, 10),
            nn.ReLU(),
            nn.Linear(10, 2),
        )

    def forward(self, x):
        # x = self.flatten(x)
        h0 = torch.randn(2, 1, 10).to(device)
        (output, h_n) = self.GRU(x, h0)
        data = self.flatten(h_n.transpose(0, 1))
        logits = self.GRU_relu_stack(data)
        return logits


PATH = "GRU_model.pt"
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print("Using {} device".format(device))


model = NeuralNetwork().to(device)
model.load_state_dict(torch.load(PATH))
model.eval()
print(model)

input_test_data = torch.randn(1, 1, 1001).to(device)
output = model(input_test_data)
print(output)
