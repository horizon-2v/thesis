import os.path
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from pyts.image import GramianAngularField
import pandas as pd
from PIL import Image
import torch
from torchvision import transforms
from tqdm import tqdm

image_size = 166
gasf = GramianAngularField(image_size=image_size, method='summation')
toPIL = transforms.ToPILImage()
min_max_scaler = preprocessing.MinMaxScaler()


def data_to_pic(pic_path, output_path):
    df = pd.read_csv(pic_path)
    pic_matrix = torch.zeros([3, 166, 166])

    for i in range(3):
        pic_matrix[i] = torch.tensor(gasf.fit_transform(df.iloc[:, i].values.reshape(1, -1)))

    pic = toPIL(pic_matrix)
    _, filename_full = os.path.split(pic_path)
    filename, _ = os.path.splitext(filename_full)
    filename += '.jpg'
    pic.save(os.path.join(output_path, filename))


def grim_to_pic(pic_path, output_path):
    df = pd.read_csv(pic_path)
    pic_matrix = torch.zeros([3, 166, 166])

    for i in range(3):
        data_vector = torch.tensor(df.iloc[:, i].values.reshape(-1, 1))
        pic_matrix[i] = data_vector * data_vector.t()
    pic = toPIL(pic_matrix)
    _, filename_full = os.path.split(pic_path)
    filename, _ = os.path.splitext(filename_full)
    filename += 'grim.jpg'
    pic.save(os.path.join(output_path, filename))


if __name__ == '__main__':
    # data_to_pic('D:\\workspace\\Python\\thesis\\new_dataset\\positive_data\\1.csv', 'D:\\科研\\学位论文\\图')
    grim_to_pic('D:\\workspace\\Python\\thesis\\new_dataset\\negative_data\\000_1.csv', 'D:\\科研\\学位论文\\图')
