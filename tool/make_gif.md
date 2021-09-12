```python
import imageio
import os

Folder = 'data_dir/any_folder_demo/bunny_canney'

imgs = []
for filename in os.listdir(Folder):
    img = imageio.imread(os.path.join(Folder, filename))
    imgs.append(img)

imageio.mimwrite('2.gif', imgs)
```
