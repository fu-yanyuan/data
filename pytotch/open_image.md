imageio and pillow
===

```python
import imageio
from PIL import Image
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

image = imageio.imread("/home/ubuntu/workspace/ARF-svox2/data/styles/8.jpg")
print(type(image))
print(image.size)
print(image.shape)


image2 = Image.open("/home/ubuntu/workspace/ARF-svox2/data/styles/8.jpg")
print(type(image2))
print(image2.size)
# print(image2.shape) # AttributeError: shape


style_img = torch.from_numpy(image).to(device=device)
print(style_img.shape)
print(type(style_img))

style_img2 = torch.from_numpy(image2).to(device=device)
print(style_img2.shape)
print(type(style_img2))
```

```shell
<class 'imageio.core.util.Array'>
90000
(300, 300)
<class 'PIL.JpegImagePlugin.JpegImageFile'>
(300, 300)
torch.Size([300, 300])
<class 'torch.Tensor'>
Traceback (most recent call last):
  File "test.py", line 22, in <module>
    style_img2 = torch.from_numpy(image2).to(device=device)
TypeError: expected np.ndarray (got JpegImageFile)
```

