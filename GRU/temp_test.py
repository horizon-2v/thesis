import pandas as pd
import torch


a = torch.Tensor([1, 2, 3]).reshape((1, -1))
b = torch.Tensor([1, 2, 3]).reshape((-1, 1))
c = a / b
print(a)
print(b)
print(c)
