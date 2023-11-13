import torch
import torch.nn.functional as F
import os
import pandas as pd
from torch.utils.data import Dataset
from torch.utils.data.dataset import T_co
from torch.utils.data import DataLoader
from torch import nn
from utils import read_split_data, train_one_epoch, evaluate
from my_dataset import MyDataSet


def input_transform(input_data):
    data = torch.as_tensor(input_data).float()
    return data


def label_transform(input_data):
    data = torch.as_tensor(input_data).long()
    return data


class CustomDataset(Dataset):
    def __init__(self, annotation_file, data_dir, transform=input_transform, target_transform=label_transform):
        self.labels = pd.read_csv(annotation_file, usecols=[1, 2])
        self.dir = data_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index) -> T_co:
        data_path = os.path.join(self.dir, self.labels.iloc[index, 0])
        data = pd.read_csv(data_path).values
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
        self.GRU_relu_stack = nn.Sequential(
            nn.Linear(300, 512),
            nn.ReLU(),
            nn.Linear(512, 1200),
            nn.ReLU(),
            nn.Linear(1200, 2048),
            nn.ReLU(),
            nn.Linear(2048, 3000),
            nn.ReLU(),
            nn.Linear(3000, 900),
            nn.ReLU(),
            nn.Linear(900, 300),
            nn.ReLU(),
            nn.Linear(300, 150),
            nn.ReLU(),
            nn.Linear(150, 60),
            nn.ReLU(),
            nn.Linear(60, 2),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.GRU_relu_stack(x)
        return logits

#
# training_data = CustomDataset(annotation_file='D:\\workspace\\Python\\GRU\\Training_annotation.csv',
#                               data_dir='D:\\workspace\\Python\\GRU\\Training_Set')
#
#
# test_data = CustomDataset(annotation_file='D:\\workspace\\Python\\GRU\\Test_annotation.csv',
#                               data_dir='D:\\workspace\\Python\\GRU\\Test_Set')
# (train_images_path, train_images_label, val_images_path, val_images_label) \
#     = read_split_data("D:\\workspace\\Python\\GRU\\new_dataset")
# val_images_path = val_images_path[0:-2]
# # val_images_label = val_images_label[0:-2]
#
# training_data = MyDataSet(images_path=train_images_path, images_class=train_images_label, transform=input_transform)
# val_dataset = MyDataSet(images_path=val_images_path, images_class=val_images_label, transform=input_transform)
#
#
# def train_loop(dataloader, model, loss_fn, optimizer):
#     size = len(dataloader.dataset)
#     for batch, (x, y) in enumerate(dataloader):
#         pred = model(x.to(device))
#         loss = loss_fn(pred, y.to(device))
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
#
#         if batch % 40 == 0:
#             loss, current = loss.item(), batch * len(x)
#             print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
#
#
# def test_loop(dataloader, model, loss_fn, accuracy_list, avg_loss_list):
#     size = len(dataloader.dataset)
#     num_batches = len(dataloader)
#     test_loss, correct = 0, 0
#
#     with torch.no_grad():
#         for x, y in dataloader:
#             pred = model(x.to(device))
#             test_loss += loss_fn(pred, y.to(device)).item()
#             correct += (pred.argmax(1) == y.to(device)).type(torch.float).sum().item()
#
#     test_loss /= num_batches
#     correct /= size
#     print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
#     accuracy_list.append(f'{(100*correct):>0.1f}%')
#     avg_loss_list.append(f'{test_loss:>8f}')
#
#
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# print("Using {} device".format(device))
#
# learning_rate = 5e-4
# batch_size = 8
# epochs = 10
#
# train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)
# test_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True)
#
#
#
# model = NeuralNetwork().to(device)
# print(model)
# loss_fn = nn.CrossEntropyLoss().to(device)
# optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
#
# accuracy = []
# loss = []
#
# for t in range(epochs):
#     print(f"Epoch {t+1}\n-------------------------------")
#     train_loop(train_dataloader, model, loss_fn, optimizer)
#     test_loop(test_dataloader, model, loss_fn, accuracy, loss)
#
# # PATH = "GRU_model.pt"
# # torch.save(model.state_dict(), PATH)
#
# # PATH = f'Training Result\\model\\GRU_e-{epochs}_r-{learning_rate}_b-{batch_size}.pt'
# # torch.save(model.state_dict(), PATH)
# #
# result_data = {'Accuracy': accuracy, 'Avg loss': loss}
# pd.DataFrame(result_data).to_csv(f'Training Result\\result\\result e-{epochs}_r-{learning_rate}_b-{batch_size}.csv',
#                                  index=False)
#
# print("Done!")



# for i in range(data.__len__()):
#     negative = data.__getitem__(i)[0]
#     arr_max = np.max(negative)
#     arr_min = np.min(negative)
#     row = len(negative)
#     clo = len(negative[0])
#     for j in range(row):
#         for k in range(clo):
#             negative[j][k] = np.random.uniform(arr_min, arr_max)
#     pd.DataFrame(negative).to_csv(f'C:\\Users\\admin\\Desktop\\TEST\\Testerror\\{i}.csv')











