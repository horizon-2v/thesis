import torch
from torchstat import stat
from thop import profile
from model import convnext_Test as creat_model
from model import convnext_tiny
from ptflops import get_model_complexity_info

Fire_model = creat_model(num_classes=2)
T_model = convnext_tiny(num_classes=2)
with torch.cuda.device(0):
    macs, params = get_model_complexity_info(Fire_model, (3, 100, 100), as_strings=True,
                                           print_per_layer_stat=True, verbose=True)
    print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
    print('{:<30}  {:<8}'.format('Number of parameters: ', params))


