Pytorch useage
---  
[torch.cat()&torch.stack()](https://zhuanlan.zhihu.com/p/148019451)
```python
c1 = torch.rand(2,3)
print(c1)
c = torch.cat([c1,c1,c1], 0)
print(c)
c = torch.cat([c1,c1,c1], 1)
print(c)
c = torch.cat([c1,c1,c1], -1) # -1 means last dimension
print(c)
```
