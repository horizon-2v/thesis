import pandas as pd
import numpy as np
import os
from tqdm import tqdm

path_dir = 'D:\\workspace\\Python\\thesis'


# 生成000负样本
# for i in tqdm(range(859)):
#     data = {'C': np.random.normal(0.5, 1.0 / 36, 162), 'S': np.random.normal(0.5, 1.0 / 36, 162),
#             'T': np.random.normal(20, 0.09, 162)}
#     output_name = os.path.join(path_dir, 'negative_data', f'000_{i+1}.csv')
#     df = pd.DataFrame(data).to_csv(output_name, index=False)


# 生成001负样本
for i in range(857):
    s = np.random.randint(1, 41)  # s: 1-40
    x = np.random.randint(1, 6)  # x: 1-5
    y = np.random.randint(1, 6)  # y: 1-5
    t = np.random.randint(0, 54)  # t: 0-53

    random_target = f'{s}_({x},{y})_{t}.csv'
    path = os.path.join(path_dir, 'data', random_target)
    positive_col = np.squeeze(pd.read_csv(path, usecols=[3]).values)
    data = {'C': np.random.normal(0.5, 1.0 / 36, 162), 'S': np.random.normal(0.5, 1.0 / 36, 162),
            'T': positive_col}
    output_name = os.path.join(path_dir, 'negative_data', f'001_{i+1}.csv')
    df = pd.DataFrame(data).to_csv(output_name, index=False)


# 生成010负样本
# for i in range(7714):
#     s = np.random.randint(1, 41)  # s: 1-40
#     x = np.random.randint(1, 6)  # x: 1-5
#     y = np.random.randint(1, 6)  # y: 1-5
#     t = np.random.randint(0, 54)  # t: 0-53
#
#     random_target = f'{s}_({x},{y})_{t}.csv'
#     path = os.path.join(path_dir, 'data', random_target)
#     positive_col = np.squeeze(pd.read_csv(path, usecols=[2]).values) * 1e+6
#     data = {'C': np.random.normal(0.5, 1.0 / 36, 18), 'S': positive_col,
#             'T': np.random.normal(20, 0.09, 18)}
#     output_name = os.path.join(path_dir, 'negative_data', f'010_{i+1}.csv')
#     df = pd.DataFrame(data).to_csv(output_name, index=False)
#     print(f'process: {(i+1)/7714.0 * 100}%')


# 生成100负样本
# for i in range(7714):
#     s = np.random.randint(1, 41)  # s: 1-40
#     x = np.random.randint(1, 6)  # x: 1-5
#     y = np.random.randint(1, 6)  # y: 1-5
#     t = np.random.randint(0, 54)  # t: 0-53
#
#     random_target = f'{s}_({x},{y})_{t}.csv'
#     path = os.path.join(path_dir, 'data', random_target)
#     positive_col = np.squeeze(pd.read_csv(path, usecols=[1]).values) * 1e+6
#     data = {'C': positive_col, 'S': np.random.normal(0.5, 1.0 / 36, 18),
#             'T': np.random.normal(20, 0.09, 18)}
#     output_name = os.path.join(path_dir, 'negative_data', f'100_{i+1}.csv')
#     df = pd.DataFrame(data).to_csv(output_name, index=False)
#     print(f'process: {(i+1)/7714.0 * 100:.2f}%')


# 生成011负样本
# for i in range(7714):
#     s = np.random.randint(1, 41)  # s: 1-40
#     x = np.random.randint(1, 6)  # x: 1-5
#     y = np.random.randint(1, 6)  # y: 1-5
#     t = np.random.randint(0, 54)  # t: 0-53
#
#     random_target = f'{s}_({x},{y})_{t}.csv'
#     path = os.path.join(path_dir, 'positive_data', random_target)
#     df = pd.read_csv(path, usecols=[1, 2, 3])
#     df[f'({x},{y})C'] = np.random.normal(0.5, 1.0 / 36, 18)
#     df.columns = ['C', 'S', 'T']
#     print(df)
#     output_name = os.path.join(path_dir, 'negative_data', f'011_{i+1}.csv')
#     df.to_csv(output_name, index=False)
#     print(f'process: {(i+1)/7714.0 * 100:.2f}%')


# 生成101负样本
# for i in range(7714):
#     s = np.random.randint(1, 41)  # s: 1-40
#     x = np.random.randint(1, 6)  # x: 1-5
#     y = np.random.randint(1, 6)  # y: 1-5
#     t = np.random.randint(0, 54)  # t: 0-53
#
#     random_target = f'{s}_({x},{y})_{t}.csv'
#     path = os.path.join(path_dir, 'positive_data', random_target)
#     df = pd.read_csv(path, usecols=[1, 2, 3])
#     df[f'({x},{y})S'] = np.random.normal(0.5, 1.0 / 36, 18)
#     df.columns = ['C', 'S', 'T']
#     # print(df)
#     output_name = os.path.join(path_dir, 'negative_data', f'101_{i+1}.csv')
#     df.to_csv(output_name, index=False)
#     print(f'process: {(i+1)/7714.0 * 100:.2f}%')


# 生成110负样本
# for i in range(7714):
#     s = np.random.randint(1, 41)  # s: 1-40
#     x = np.random.randint(1, 6)  # x: 1-5
#     y = np.random.randint(1, 6)  # y: 1-5
#     t = np.random.randint(0, 54)  # t: 0-53
#
#     random_target = f'{s}_({x},{y})_{t}.csv'
#     path = os.path.join(path_dir, 'positive_data', random_target)
#     df = pd.read_csv(path, usecols=[1, 2, 3])
#     df[f'({x},{y})T'] = np.random.normal(20, 0.09, 18)
#     df.columns = ['C', 'S', 'T']
#     # print(df)
#     output_name = os.path.join(path_dir, 'negative_data', f'110_{i+1}.csv')
#     df.to_csv(output_name, index=False)
#     print(f'process: {(i+1)/7714.0 * 100:.2f}%')

