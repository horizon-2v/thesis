import pandas as pd
import numpy as np
import os
from tqdm import tqdm
import random

path_dir = 'D:\\workspace\\Python\\thesis\\new_dataset'


# # 生成000负样本
# for i in tqdm(range(330)):
#     data = {'S': np.random.normal(0.5, 1.0 / 36, 166), 'C': np.random.normal(0.5, 1.0 / 36, 166),
#             'T': np.random.normal(20, 0.09, 166)}
#     output_name = os.path.join(path_dir, 'negative_data', f'000_{i+1}.csv')
#     df = pd.DataFrame(data).to_csv(output_name, index=False)


# # 生成001负样本
# for i in tqdm(range(326)):
#     positive_list = os.listdir(os.path.join(path_dir, 'positive_data'))
#     path = random.sample(positive_list, k=1)
#     positive_col = np.squeeze(pd.read_csv(os.path.join(path_dir, 'positive_data', path[0]), usecols=[2]).values)
#     data = {'S': np.random.normal(0.5, 1.0 / 36, 166), 'C': np.random.normal(0.5, 1.0 / 36, 166),
#             'T': positive_col}
#     output_name = os.path.join(path_dir, 'negative_data', f'001_{i+1}.csv')
#     df = pd.DataFrame(data).to_csv(output_name, index=False)


# # 生成010负样本
# for i in tqdm(range(326)):
#     positive_list = os.listdir(os.path.join(path_dir, 'positive_data'))
#     path = random.sample(positive_list, k=1)
#     positive_col = np.squeeze(pd.read_csv(os.path.join(path_dir, 'positive_data', path[0]), usecols=[0]).values)
#     data = {'S': positive_col, 'C': np.random.normal(0.5, 1.0 / 36, 166),
#             'T': np.random.normal(20, 0.09, 166)}
#     output_name = os.path.join(path_dir, 'negative_data', f'010_{i+1}.csv')
#     df = pd.DataFrame(data).to_csv(output_name, index=False)


# # 生成100负样本
# for i in tqdm(range(326)):
#     positive_list = os.listdir(os.path.join(path_dir, 'positive_data'))
#     path = random.sample(positive_list, k=1)
#     positive_col = np.squeeze(pd.read_csv(os.path.join(path_dir, 'positive_data', path[0]), usecols=[1]).values)
#     data = {'S': np.random.normal(0.5, 1.0 / 36, 166), 'C': positive_col,
#             'T': np.random.normal(20, 0.09, 166)}
#     output_name = os.path.join(path_dir, 'negative_data', f'100_{i+1}.csv')
#     df = pd.DataFrame(data).to_csv(output_name, index=False)


# 生成011负样本
# for i in tqdm(range(326)):
#     positive_list = os.listdir(os.path.join(path_dir, 'positive_data'))
#     path = random.sample(positive_list, k=1)
#     df = pd.read_csv(os.path.join(path_dir, 'positive_data', path[0]))
#     df.iloc[0:, [1]] = pd.DataFrame(np.random.normal(0.5, 1.0 / 36, 166))
#     df.columns = ['S', 'C', 'T']
#     output_name = os.path.join(path_dir, 'negative_data', f'011_{i+1}.csv')
#     df.to_csv(output_name, index=False)


# # 生成101负样本
# for i in tqdm(range(326)):
#     positive_list = os.listdir(os.path.join(path_dir, 'positive_data'))
#     path = random.sample(positive_list, k=1)
#     df = pd.read_csv(os.path.join(path_dir, 'positive_data', path[0]))
#     df.iloc[0:, [0]] = pd.DataFrame(np.random.normal(0.5, 1.0 / 36, 166))
#     df.columns = ['S', 'C', 'T']
#     output_name = os.path.join(path_dir, 'negative_data', f'101_{i+1}.csv')
#     df.to_csv(output_name, index=False)


# 生成110负样本
for i in tqdm(range(326)):
    positive_list = os.listdir(os.path.join(path_dir, 'positive_data'))
    path = random.sample(positive_list, k=1)
    df = pd.read_csv(os.path.join(path_dir, 'positive_data', path[0]))
    df.iloc[0:, [2]] = pd.DataFrame(np.random.normal(20, 0.09, 166))
    df.columns = ['S', 'C', 'T']
    output_name = os.path.join(path_dir, 'negative_data', f'110_{i+1}.csv')
    df.to_csv(output_name, index=False)

