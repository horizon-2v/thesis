import pandas as pd
import os
import numpy as np
from tqdm import tqdm

output_path = ".\\new_dataset\\positive_data"
path = "C:\\Users\\admin\\Desktop\\dataSet_new\\Training Set\\positive"

count = 0
file_list = os.listdir(path)
for file in tqdm(file_list):
    df = pd.read_csv(os.path.join(path, file), usecols=[1, 2, 3])
    for i in range(6):
        count += 1
        output_df = df.iloc[i*166:i*166+166].to_csv(os.path.join(output_path, f'{count}.csv'), index=False)



