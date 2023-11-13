import numpy as np
import pandas as pd
import os
from tqdm import tqdm

for index in tqdm(range(40)):
    path_dir = 'D:\\workspace\\Python\\thesis'
    path = os.path.join(path_dir, 'raw_data', str(index + 1) + '.csv')
    df = pd.read_csv(path, header=1)
    for i in range(6):
        for j in range(5):
            for k in range(5):
                # print(df.loc[20 + i * 18:37 + i * 18,
                #       ['Time', f'({j+1},{k+1})C', f'({j+1},{k+1})S', f'({j+1},{k+1})T']])
                output_name = os.path.join(path_dir, 'positive_data', str(index + 1) + f'_({j + 1},{k + 1})_{i}.csv')
                output_df = df.loc[20 + i * 162:181 + i * 162, [f'({j + 1},{k + 1})C', f'({j + 1},{k + 1})S',
                                                                f'({j + 1},{k + 1})T']]
                col = output_df.columns.tolist()
                row = output_df.index.tolist()
                coefficient_data = np.ones((3, 162))
                coefficient_data[0:2] = coefficient_data[0:2] * 1e+6
                Coefficient = pd.DataFrame(coefficient_data.T, columns=col, index=row)
                output_df = output_df * Coefficient
                output_df.to_csv(output_name, index=False)
