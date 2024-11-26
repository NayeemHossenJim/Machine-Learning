import numpy as np 
import matplotlib.pyplot as plt

x = np.random.randint(2,50, size=(25))
y = np.random.randint(2,50, size=(25))
color = np.random.randint(2,50, size=(25))

plt.scatter(x,y,c=color,cmap="viridis")
plt.show()