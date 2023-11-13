import pandas
import matplotlib.pyplot as plt

import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
data = np.transpose(pandas.read_excel(io=r'D:\\科研\\学位论文\\专利\\训练结果.xlsx', header=None).values.tolist())


if __name__ == '__main__':
    X = range(1, len(data[0]) + 1, 1)
    Y1 = data[0]
    Y2 = data[1]

    fig, ax1 = plt.subplots()
    plt.xticks(X[::2])

    ax1.plot(X, Y1, 'o-', color="blue", label="Accuracy",)
    ax1.set_xlabel("epoch")
    ax1.set_ylabel("Accuracy(%)")

    ax2 = ax1.twinx()
    ax2.plot(X, Y2, 'v-', color="red", label="CrossEntropyLoss")
    ax2.set_ylabel("CrossEntropyLoss")

    fig.legend(loc="upper right", bbox_to_anchor=(1.015, 1.155), bbox_transform=ax1.transAxes)
    plt.grid(axis='both')
    plt.show()

