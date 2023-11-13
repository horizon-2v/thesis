import pymannkendall as mk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import os
from tqdm import tqdm

path = "D:\\workspace\\Python\\thesis\\new_dataset\\positive_data"
index = os.listdir(path)
count = 0
for name in tqdm(index):
    data = pd.read_csv(os.path.join(path, name), usecols=[0]).values.squeeze()
    result = mk.original_test(data, alpha=0.05)
    if result.h:
        count += 1

path = "D:\\workspace\\Python\\thesis\\new_dataset\\negative_data"
index = os.listdir(path)
for name in tqdm(index):
    data = pd.read_csv(os.path.join(path, name), usecols=[0]).values.squeeze()
    result = mk.original_test(data, alpha=0.05)
    if not result.h:
        count += 1

mk = 1.0 * count / (2 * len(index))
print(mk)



# data = preprocessing.scale(data)
# result = mk.original_test(data, alpha=0.05)
# print(result)

# time = pd.read_csv("C:\\Users\\admin\\Desktop\\data\\data\\TrainingSet\\1_(1,1).csv", usecols=[0]).values.squeeze()[20:]
# time -= 1.21
# z = []
# x = []
# slope = []
# index = 0
# step = 163
# while index + step <= 980:
#     result = mk.original_test(data[index:index + step], alpha=0.05)
#     z.append(result.z)
#     x.append(time[index + step])
#     slope.append(result.slope)
#     index += step
# print(x)
# print(z)
# print(slope)

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# h1, = ax.plot(time, data, 'r,-', alpha=0.5, linewidth=2, label='CO')
# ax.set_ylabel('CO', fontsize=15)
# ax.set_title("Mann-Kendall", size=16)
# ax.set_xlabel('Time', fontsize=15)
#
# ax2 = ax.twinx()
# h2, = ax2.plot(x, z, 'b^-.', alpha=0.5, linewidth=2, label='Z')
# ax2.set_ylabel('Z', fontsize=15)
#
# ax.tick_params(axis='x', labelsize=13)
# ax.tick_params(axis='y', colors='r', labelsize=13)
# ax2.tick_params(axis='y', colors='b', labelsize=13)
# ax.yaxis.label.set_color('r')
# ax2.yaxis.label.set_color('b')
#
# plt.rcParams.update({'font.size': 15})
# ax.legend([h1, h2], ['CO', 'Z'], loc=4)
# plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# h1, = ax.plot(time, data, 'r,-', alpha=0.5, linewidth=2, label='CO')
# ax.set_ylabel('CO', fontsize=15)
# ax.set_title("Theil-Sen", size=16)
# ax.set_xlabel('Time', fontsize=15)
#
# ax2 = ax.twinx()
# h2, = ax2.plot(x, slope, 'm^-.', alpha=0.5, linewidth=2, label='z')
# ax2.set_ylabel('Slope', fontsize=15)
#
# ax.tick_params(axis='x', labelsize=13)
# ax.tick_params(axis='y', colors='r', labelsize=13)
# ax2.tick_params(axis='y', colors='m', labelsize=13)
# ax.yaxis.label.set_color('r')
# ax2.yaxis.label.set_color('m')
#
# plt.rcParams.update({'font.size': 15})
# ax.legend([h1, h2], ['CO', 'Slope'], loc=4)
# plt.show()



