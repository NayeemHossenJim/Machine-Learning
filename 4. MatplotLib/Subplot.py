import numpy as np 
import matplotlib.pyplot as plt 

x = ([1,3,4,7,8,9])
y = ([2,4,6,7,6,2])

plt.subplot(2,2,1)
plt.plot(y, 'o-.r')

plt.subplot(2,2,2)
plt.plot(x, 'o-.b')

plt.subplot(2,2,3)
plt.plot(y, 'o-.b')

plt.subplot(2,2,4)
plt.plot(x, 'o-.b')

plt.show()