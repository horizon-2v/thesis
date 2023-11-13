import torch

x = torch.tensor([[[[1,  2], [3,  4]], [[5,  6], [7,  8]]], [[[4,  2], [1,  3]], [[8,  6], [5,  7]]]],
                 dtype=torch.float64)
mean = x.mean(dim=(0, 1), keepdim=True)
print(x)
print(mean)
