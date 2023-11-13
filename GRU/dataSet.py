import os
from shutil import copy  # shutil 是用来复制黏贴文件的
import random
import numpy as np
import pandas as pd


def dataset_generator(original_dir, original_path, process):
    training_dir = 'D:\\workspace\\Python\\GRU\\Training_Set'
    test_dir = 'D:\\workspace\\Python\\GRU\\Test_Set'
    for filename in original_dir[:43200]:
        process += 1
        print(f'process: {(process / 108000.0) * 100:.4f}%')
        from_path = os.path.join(original_path, filename)  # 旧文件的绝对路径(包含文件的后缀名)
        to_path = os.path.join(training_dir, filename)  # 新文件的绝对路径
        copy(from_path, to_path)  # 完成复制黏贴

    for filename in original_dir[43200:]:
        process += 1
        print(f'process: {(process / 108000.0) * 100:.4f}%')
        from_path = os.path.join(original_path, filename)  # 旧文件的绝对路径(包含文件的后缀名)
        to_path = os.path.join(test_dir, filename)  # 新文件的绝对路径
        copy(from_path, to_path)  # 完成复制黏贴


positive_path = 'D:\\workspace\\Python\\GRU\\positive_data'
negative_path = 'D:\\workspace\\Python\\GRU\\negative_data'  # 想拆分的文件夹所在路径,也就是一大堆文件所在的路径
save_dir = 'D:\\workspace\\Python\\GRU'

positive_dir = os.listdir(positive_path)  # os.listdir(file_path) 是获取指定路径下包含的文件或文件夹列表
random.shuffle(positive_dir)
negative_dir = os.listdir(negative_path)
random.shuffle(negative_dir)

dataset_generator(positive_dir, positive_path, 0)
dataset_generator(negative_dir, negative_path, 54000)

training_positive = {'data': positive_dir[:43200], 'label': np.ones(43200)}
test_positive = {'data': positive_dir[43200:], 'label': np.ones(10800)}
training_negative = {'data': negative_dir[:43200], 'label': np.zeros(43200)}
test_negative = {'data': negative_dir[43200:], 'label': np.zeros(10800)}

training_df = pd.concat([pd.DataFrame(training_positive), pd.DataFrame(training_negative)], ignore_index=True)
test_df = pd.concat([pd.DataFrame(test_positive), pd.DataFrame(test_negative)], ignore_index=True)
print(training_df)
print(test_df)

training_df.to_csv(os.path.join(save_dir, 'Training_annotation.csv'))
test_df.to_csv(os.path.join(save_dir, 'Test_annotation.csv'))


