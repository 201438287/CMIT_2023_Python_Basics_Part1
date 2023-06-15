import numpy as np
import matplotlib.pyplot as plt
#cut the interval equally into num parts
T=np.linspace(0,2*np.pi, num=500)
R=10
X=[]
Y=[]
for t in T:
    X.append(R*(t-np.sin(t)))
    Y.append(R*(1-np.cos(t)))

plt.plot(X,Y)
plt.savefig("Cycloid.eps")
plt.close()

