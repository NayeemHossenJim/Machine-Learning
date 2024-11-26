import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,5,7,8])
y = np.array([2,5,6,2,8])

plt.plot(x,y,'D-.r',ms=5,mec='k',mfc='g')
plt.show()