import torch
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.utils import save_image

image_size = 256
batch_size = 41
nc = 3

my_transforms=transforms.Compose([
                                  transforms.Resize(image_size),
                                  transforms.CenterCrop(image_size), # w/o this, we can not get a square image
                                  transforms.ToTensor()
])

dataroot = "/home/ubuntu/workspace/datasets/nerf_llff_data/room" # Root directory for dataset
dataset = datasets.ImageFolder(root=dataroot, transform=my_transforms)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size)

img_num = 0
for img in dataset:
    img_num += 1
    print(img_num)
    print(img[0].shape)
    save_image(img[0], 'data/llff_room_resized/img'+str(img_num)+'.png')



# transforms=transforms.Compose([
#                                transforms.Resize(image_size),
#                                transforms.CenterCrop(image_size),  # w/o this, we can not get a square image
#                                transforms.ToTensor(),
#                                transforms.Normalize([0.5 for _ in range(nc)], [0.5 for _ in range(nc)]),
#                            ])

# dataroot = "/home/ubuntu/workspace/datasets/celeba" # Root directory for dataset
# # If you train on MNIST, remember to set channels_img to 1
# # dataset = datasets.MNIST(root="dataset/", train=True, transform=transforms, download=False)
# dataset = datasets.ImageFolder(root=dataroot, transform=transforms)
# dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size,
#                                          shuffle=True)


# for i, data in enumerate(dataloader):
#     print(data[i])
#     print(data[i].shape)
