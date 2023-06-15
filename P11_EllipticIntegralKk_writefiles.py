import numpy as np
import math
#Trapezium
def Khalf(theta):
    d=4-math.pow(np.sin(theta),2)
    y=2/(math.pow(d,1/2))
    return y

T=np.linspace(0,np.pi/2, num=500)
#increment in theta
dt=T[1]-T[0]
K=[]
for t in T:
    K.append(Khalf(t))
f=open("EllipticIntegralKk_writefiles.txt","w")
for k in K:
    f.write(str(k)+"\n")
f.close()
