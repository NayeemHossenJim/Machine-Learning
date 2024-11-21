import numpy as nb

a = nb.array([[2,3,4],[4,5,6]])
b = nb.array([[4,2],[5,4],[7,8]])

c = nb.matmul(b,a)
print(c)