import numpy as np
import matplotlib.pyplot as plt
#cut the interval equally into num parts
T=np.linspace(0,2*np.pi, num=500)
R=10
X=R*(T-np.sin(T))
Y=R*(1-np.cos(T))
#X=[]
#Y=[]
#for t in T:
#    X.append(R*(t-np.sin(t)))
#    Y.append(R*(1-np.cos(t)))

#plt.subplot(1,2,1); plt.plot(X,Y)
#plt.subplot(1,2,2); plt.plot(X,-np.array(Y)/4)
plt.subplot(2,1,1); plt.plot(X,Y)
plt.subplot(2,1,2); plt.plot(X,-np.array(Y)/4)
plt.savefig("SubplotExampleCycloid.eps")
plt.close()
