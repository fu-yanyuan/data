```python
from PIL import Image
import os
import cv2
import numpy as np
import imageio

Folder = '/home/ubuntu/workspace/ARF-svox2/data/llff/room/images_4'
SaveF = '/home/ubuntu/workspace/ARF-svox2/data/llff/roomgray/images_4'

if not os.path.exists(SaveF):
    os.makedirs(SaveF)

for name in os.listdir(Folder):
    img = cv2.imread(os.path.join(Folder, name))
    # img.save(os.path.join(SaveF, name))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = np.zeros_like(img)
    img2[:,:,0] = gray
    img2[:,:,1] = gray
    img2[:,:,2] = gray
    cv2.imwrite(os.path.join(SaveF, name), img2)

img = imageio.imread('/home/ubuntu/workspace/ARF-svox2/data/llff/roomgray/images_4/DJI_20200226_143850_006.png')
print(img.shape)

# import cv2
# import numpy as np
# img = cv2.imread("/home/ubuntu/workspace/ARF-svox2/data/styles/8.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img2 = np.zeros_like(img)
# img2[:,:,0] = gray
# img2[:,:,1] = gray
# img2[:,:,2] = gray
# cv2.imwrite("/home/ubuntu/workspace/ARF-svox2/data/styles/8_3channel.jpg", img2)
```
