import os
import pandas as pd
import numpy as np
import random

positive_path = 'D:\\workspace\\Python\\GRU\\positive_data'  # 想拆分的文件夹所在路径,也就是一大堆文件所在的路径
negative_path = 'D:\\workspace\\Python\\GRU\\negative_data'  # 想拆分的文件夹所在路径,也就是一大堆文件所在的路径

save_dir = 'D:\\workspace\\Python\\GRU'  # save_dir 是想把复制出来的文件存放在的路径

positive_data = os.listdir(positive_path)
negative_data = os.listdir(negative_path)

training_positive = {'data': positive_data[:43200], 'label': np.ones(43200)}
test_positive = {'data': positive_data[43200:], 'label': np.ones(10800)}
training_negative = {'data': negative_data[:43200], 'label': np.zeros(43200)}
test_negative = {'data': negative_data[43200:], 'label': np.zeros(10800)}

training_df = pd.concat([pd.DataFrame(training_positive), pd.DataFrame(training_negative)], ignore_index=True)
test_df = pd.concat([pd.DataFrame(test_positive), pd.DataFrame(test_negative)], ignore_index=True)
print(training_df)
print(test_df)

training_df.to_csv(os.path.join(save_dir, 'Training_annotation.csv'))
test_df.to_csv(os.path.join(save_dir, 'Test_annotation.csv'))

