import math

import pymannkendall as mk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np
import random

path = "D:\\科研\\学位论文\\图\\2-2-1\\仿真结果\\传感器仿真数据.xlsx"
# path = "C:\\Users\\admin\\Desktop\\data\\data\\TrainingSet\\1.csv"

smoke = pd.read_excel(path, usecols=[1], header=1).values.squeeze()
CO = pd.read_excel(path, usecols=[8], header=1).values.squeeze()
temp = pd.read_excel(path, usecols=[3], header=1).values.squeeze()

data = preprocessing.scale(temp)
time = pd.read_excel(path, usecols=[0], header=1).values.squeeze()
z_true = []
x = []
slope_true = []
index = 0
step = 166
while index + step <= 1001:
    result = mk.original_test(data[index:index + step], alpha=0.05)
    z_true.append(result.z)
    x.append(time[index + step])
    slope_true.append(result.slope)
    index += step
# print(x)
print(z_true)
print(slope_true)

noise = []
for i in range(smoke.size):
    noise.append(np.random.normal(loc=0.0, scale=1.0, size=None))

z_false = []
slope_false = []
index = 0
step = 166
while index + step <= 1001:
    result = mk.original_test(noise[index:index + step], alpha=0.05)
    z_false.append(result.z)
    x.append(time[index + step])
    slope_false.append(result.slope)
    index += step
# print(x)
print(z_false)
print(slope_false)


# path = "C:\\Users\\admin\\Desktop\\data\\data\\TrainingSet\\1.csv"
# # path = "C:\\Users\\admin\\Desktop\\data\\data\\TrainingSet\\1.csv"
#
# data = pd.read_csv(path, usecols=[2]).values.squeeze()[20:]
# data = preprocessing.scale(data)
# time = pd.read_csv("C:\\Users\\admin\\Desktop\\data\\data\\TrainingSet\\1_(1,1).csv", usecols=[0]).values.squeeze()[20:]
# time -= 1.21
# z_false = []
# slope_false = []
# index = 0
# step = 163
# while index + step <= 980:
#     result = mk.original_test(data[index:index + step], alpha=0.05)
#     z_false.append(np.log10(abs(result.z)))
#     slope_false.append(np.log10(abs(result.slope)))
#     index += step
# # print(x)
# print(z_false)
# # print(slope_false)
#
# x = [1, 2, 3, 4, 5, 6]
# for a, b in zip(x, slope_true):
#     plt.text(a, b - 0.05, "%.3f" % b, ha='center', va='top', fontsize=13)
# plt.plot(x, slope_true, 'r^-.', linewidth=2, label='True', markersize=8)
# for a, b in zip(x, slope_false):
#     plt.text(a, b - 0.05, "%.3f" % b, ha='center', va='top', fontsize=13)
# plt.plot(x, slope_false, 'bv-.', linewidth=2, label='False', markersize=8)
# plt.rcParams.update({'font.size': 15})
# plt.legend()
# plt.xlabel('Number', fontsize=15)
# plt.ylabel('log(|Slope|)', fontsize=15)
# plt.title('Theil-Sen Constrast', fontsize=16)
# plt.yticks(fontsize=13)
# plt.xticks(fontsize=13)
# plt.grid(which='major')
# plt.show()



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



