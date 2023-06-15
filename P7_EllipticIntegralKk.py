import numpy as np
import math
def Khalf(theta):
    d=4-math.pow(np.sin(theta),2)
    y=2/(math.pow(d,1/2))
    return y
#the last one does not count
T=np.linspace(0,np.pi/2, num=500)[:-1]
#increment in theta
dt=T[1]-T[0]
K=[]
for t in T:
    K.append(Khalf(t))
#integral 
I=sum(K)*dt
print(I)

