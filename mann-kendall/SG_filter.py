import scipy
import pandas as pd
import numpy as np
import random


def awgn(x, snr, seed=7):
    np.random.seed(seed)  # 设置随机种子
    snr = 10 ** (snr / 10.0)
    xpower = np.sum(x ** 2) / len(x)
    npower = xpower / snr
    noise = np.random.randn(len(x)) * np.sqrt(npower)
    return x + noise

path = "D:\\科研\\学位论文\\图\\2-2-1\\仿真结果\\传感器仿真数据.xlsx"
# path = "C:\\Users\\admin\\Desktop\\data\\data\\TrainingSet\\1.csv"

smoke = pd.read_excel(path, usecols=[1], header=1).values.squeeze()
CO = pd.read_excel(path, usecols=[8], header=1).values.squeeze()
temp = pd.read_excel(path, usecols=[3], header=1).values.squeeze()

current_data = awgn(smoke, 20)
data_length = len(current_data)
sigma = np.std(current_data)
pos = random.choice(range(data_length))
current_data[pos] += 4*sigma

smooth_data = scipy.signal.savgol_filter(current_data, 16, 5, mode='nearest')
output = np.array([current_data, smooth_data])
df = pd.DataFrame(np.transpose(output))
df.to_csv(".\\SG_filter.csv")
print(df)

