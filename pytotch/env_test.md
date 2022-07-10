```python
import torch
from torchvision import datasets
from torchvision.transforms import ToTensor

# test pytorch
print(torch.__version__) 

# test CUDA
print(torch.cuda.is_available())

# # test torchvision
# training_data2 = datasets.MNIST(
#     root='data',
#     train=True,
#     download=False,  
#     transform=ToTensor()
# )
```
