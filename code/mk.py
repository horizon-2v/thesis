import pymannkendall as mk
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np
from scipy.stats import kendalltau
from tqdm import tqdm

# path = "D:\\workspace\\Python\\thesis\\dataset\\positive_data\\1_(1,1)_3.csv"
# path = "D:\\workspace\\Python\\thesis\\dataset\\negative_data\\000_4.csv"
# data = np.transpose(pd.read_csv(path).values)
# result = mk.original_test(data[0], alpha=0.05)
# print(result)

path_dir = "D:\\workspace\\Python\\thesis\\dataset"
path = os.path.join(path_dir, "negative_data")
data_list = [os.path.join(path, data) for data in os.listdir(path)]
result = []
for data_path in tqdm(data_list):
    data = np.transpose(pd.read_csv(data_path).values)
    result.append(mk.original_test(data[0], alpha=0.05).trend)
print(result)
# c = data[0]
# s = data[1]
# t = data[2]
#
# print(kendalltau(c, s))
# print(kendalltau(c, t))
# print(kendalltau(s, t))
