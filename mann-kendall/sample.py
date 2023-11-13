from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from tqdm import tqdm

path = 'D:\\workspace\\Python\\thesis\\new_dataset\\negative_data'
output_path = 'C:\\Users\\admin\\Desktop\\new_dataset\\negative data'
file_list = os.listdir(path)

for file in tqdm(file_list):
    re_matrix = np.zeros((100, 3))
    for i in range(3):
        data = pd.read_csv(os.path.join(path, file), usecols=[i]).values.squeeze()
        re_data = signal.resample(data, 100)
        re_data[0:5] = data[0:5]
        re_matrix[:, i] = re_data
    df = pd.DataFrame(re_matrix)
    df.columns = ['S', 'C', 'T']
    df.to_csv(os.path.join(output_path, file), index=False)

# plt.plot(smoke, 'b*--', label='raw data')
# plt.plot(re_smoke, 'r.--', label='resample data')
# plt.legend()
# plt.show()
