import os.path
import random
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GramianAngularField
import pandas as pd
from PIL import Image
import torch
from torchvision import transforms
from tqdm import tqdm


image_size = 100
gasf = GramianAngularField(image_size=image_size, method='summation')
toPIL = transforms.ToPILImage()
path = "new_dataset"
positive_output_path = 'new_pic_dataset\\positive_data'
negative_output_path = 'new_pic_dataset\\negative_data'


def data_to_pic(pic_path, output_path):
    df = pd.read_csv(pic_path)
    pic_matrix = torch.zeros([3, 100, 100])

    for i in range(3):
        pic_matrix[i] = torch.tensor(gasf.fit_transform(df.iloc[:, i].values.reshape(1, -1)))

    pic = toPIL(pic_matrix)
    _, filename_full = os.path.split(pic_path)
    filename, _ = os.path.splitext(filename_full)
    filename += '.jpg'
    pic.save(os.path.join(output_path, filename))


# data = np.random.rand(18).reshape(1, -1)
# data_normal = np.arange(18).reshape(1, -1)
# print(data)

# image_size = 18
# gasf = GramianAngularField(image_size=image_size, method='summation')
# sin_gasf = gasf.fit_transform(data)
# gadf = GramianAngularField(image_size=image_size, method='difference')
# sin_gadf = gadf.fit_transform(data_normal)
#
# print(sin_gasf)
# print(sin_gadf)
# images = [sin_gasf[0], sin_gadf[0]]
# titles = ['Summation', 'Difference']
#
# fig, axs = plt.subplots(1, 2, constrained_layout=True)
# for image, title, ax in zip(images, titles, axs):
#     ax.imshow(image)
#     ax.set_title(title)
# fig.suptitle('GramianAngularField', y=0.94, fontsize=16)
# plt.margins(0, 0)
# plt.savefig("GramianAngularField.pdf", pad_inches=0)
# plt.show()


def generate_pic(path_dir, val_rate):
    random.seed(0)
    assert os.path.exists(path_dir), "root path: {} does not exist".format(path_dir)
    class_list = [cla for cla in os.listdir(path_dir) if os.path.isdir(os.path.join(path_dir, cla))]
    class_list.sort()

    positive_images_path = []  # 存储训练集的所有图片路径
    negative_images_path = []  # 负样本图片路径
    every_class_num = []  # 存储每个类别的样本总数
    supported = [".csv"]  # 支持的文件后缀类型
    # 遍历每个文件夹下的文件
    for cla in class_list:
        cla_path = os.path.join(path_dir, cla)
        # 遍历获取supported支持的所有文件路径
        data = [os.path.join(path_dir, cla, i) for i in os.listdir(cla_path)
                if os.path.splitext(i)[-1] in supported]
        # 排序，保证各平台顺序一致
        data.sort()
        # 记录该类别的样本数量
        every_class_num.append(len(data))
        # 按比例随机采样验证样本
        val_path = random.sample(data, k=int(len(data) * val_rate))

        for data_path in data:
            if data_path in val_path:  # 如果该路径在采样的验证集样本中则存入验证集
                if cla == 'positive_data':
                    positive_images_path.append(data_path)
                else:
                    negative_images_path.append(data_path)

    print("{} images were found in the dataset.".format(sum(every_class_num)))
    print("{} positive images.".format(len(positive_images_path)))
    print("{} negative images.".format(len(negative_images_path)))

    return positive_images_path, negative_images_path


if __name__ == '__main__':
    # positive_path, negative_path = generate_pic(path, 1)
    # for file in tqdm(positive_path):
    #     data_to_pic(file, positive_output_path)
    # for file in tqdm(negative_path):
    #     data_to_pic(file, negative_output_path)
    data_to_pic('C:\\Users\\admin\\Desktop\\TEST.csv', 'C:\\Users\\admin\\Desktop')



