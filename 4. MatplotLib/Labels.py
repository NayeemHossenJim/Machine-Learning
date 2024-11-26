import numpy as np 
import matplotlib.pyplot as plt 

x = ([1,3,4,7,8,9])
y = ([2,4,6,7,6,2])

plt.plot(x,y, 'o-.r')

f1 = {'family':'serif','color':'deeppink','size':12}
f2 = {'family':'serif','color':'black','size':12}


plt.xlabel("Days",fontdict=f1)
plt.ylabel("Gay Increased",fontdict=f1)
plt.title("LGBTQ Supporter o UU", fontdict=f2)

plt.show()