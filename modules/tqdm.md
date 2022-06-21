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

```python
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char)
```
```
Processing d: 100%|███████████████████████████████████████████████████████████████████████████████████| 4/4 [00:01<00:00,  3.98it/s]
```

the above `Processing d`, is change w.r.t the list

add total

```python
pbar = tqdm(["a", "b", "c", "d"], total=5)
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char)
```

```
Processing d:  80%|██████████████████████████████████████████████████████████████████▍                | 4/5 [00:01<00:00,  3.98it/s]
```
