import pandas as pd
import os
import numpy as np
import tqdm

output_path = "C:\\Users\\admin\\Desktop\\dataSet_new\\Training Set\\positive"
path = "C:\\Users\\admin\\Desktop\\dataSet_new\\4-2-2\\KETING"
room_label = 'C02'
file_list = os.listdir(path)

for file in file_list:
    df = pd.read_csv(os.path.join(path, file), header=1)
    for i in range(4):
        for j in range(4):
            name = os.path.join(output_path, f'4-{os.path.splitext(file)[0]}({i + 1},{j + 1}).csv')
            df[f'S({i + 1},{j + 1})-{room_label}'] = df[f'S({i + 1},{j + 1})-{room_label}'].map(lambda x: x * 10e6)
            df[f'C({i + 1},{j + 1})-{room_label}'] = df[f'C({i + 1},{j + 1})-{room_label}'].map(lambda x: x * 10e6)
            df[['Time', f'S({i + 1},{j + 1})-{room_label}', f'C({i + 1},{j + 1})-{room_label}',
                f'T({i + 1},{j + 1})-{room_label}']].to_csv(name, index=False)  # 加f支持大括号内的python表达式

# for file in file_list:
#     df = pd.read_csv(os.path.join(path, file), header=1)
#     for i in range(3):
#         for j in range(3):
#             name = os.path.join(output_path, f'2-{os.path.splitext(file)[0]}({i + 1},{j + 1})-2.csv')
#             df[f'S({i + 1},{j + 1})-{room_label}'] = df[f'S({i + 1},{j + 1})-{room_label}'].map(lambda x: x * 10e6)
#             df[f'C({i + 1},{j + 1})-{room_label}'] = df[f'C({i + 1},{j + 1})-{room_label}'].map(lambda x: x * 10e6)
#             df[['Time', f'S({i + 1},{j + 1})-{room_label}', f'C({i + 1},{j + 1})-{room_label}',
#                 f'T({i + 1},{j + 1})-{room_label}']].to_csv(name, index=False)  # 加f支持大括号内的python表达式

