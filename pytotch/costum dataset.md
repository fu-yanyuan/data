Creating a Custom Dataset for your files
---  

### structured folder
```
directory/
├── class_1
│   ├── xxx.png
│   ├── xxy.png
│   └── ...
│       
└── class_2
    ├── 123.png
    ├── nsdf3.png
    └── ...
    └── asd932_.png
```  

use `torchvision.datasets.ImageFolder()`  
this will automantically return images with labels  

### Creating a Custom Dataset for your files  
A custom Dataset class must implement three functions: `__init__, __len__, and __getitem__.`  
inherit from the Dataset class from torch.utils.data and override the `__init__, __len__ and __getitem__` methods to make it fit our dataset.  

```python
import os
import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
import PIL
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
```  

```python 
class FacesDataset(Dataset):

    def __init__(self, root, image_dir, csv_file, transform=None):
        self.root = root
        self.image_dir = image_dir
        self.image_files = os.listdir(image_dir)
        self.data = pd.read_csv(csv_file).iloc[:, 1]
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        image_name = os.path.join(self.image_dir, self.image_files[index])  
        image = PIL.Image.open(image_name)
        label = self.data[index]
        if self.transform:
            image = self.transform(image)
        return (image, label)
        
```  

```python
dset = FacesDataset(root, image_dir, csv_file, transform= transform_img)

train_dataset, test_dataset = torch.utils.data.random_split(dset, [50, 18])
```

#### read_image
read_image will return tensor, so don't need to transform the dataset toTensor()
```
import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```
