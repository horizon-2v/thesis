import torch
from torchstat import stat
from thop import profile
from model import NeuralNetwork
from ptflops import get_model_complexity_info

model = NeuralNetwork()
with torch.cuda.device(0):
    macs, params = get_model_complexity_info(model, (1, 300), as_strings=True,
                                           print_per_layer_stat=True, verbose=True)
    print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
    print('{:<30}  {:<8}'.format('Number of parameters: ', params))

