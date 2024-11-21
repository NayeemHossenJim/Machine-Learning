import numpy as nb 

a = nb.ones((5,5))
b = nb.zeros((3,3))
b[1,1] = 9

a[1:4,1:4] = b
print(a)