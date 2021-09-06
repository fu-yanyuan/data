tqdm
---  
refer to https://github.com/tqdm/tqdm for more

```python
from tqdm.notebook import tqdm

N = 1000000
for i in tqdm(range(N), desc='Training'):
    pass
```  
```
Training:   0%|          | 0/1000000 [00:00<?, ?it/s]
```
