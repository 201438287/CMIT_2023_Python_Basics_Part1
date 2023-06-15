import numpy as np
import matplotlib.pyplot as plt
import math
#total number of rotations
#from 0 to 2pi
Total=6

#degree rotating each time
Increment=2*math.pi/Total

c=math.cos(Increment)
s=math.sin(Increment)
Rotation=[[c,-s],[s,c]]
#convert list to numpy format
Rotation=np.array(Rotation)
point=np.array([1,0])
Points=[[1,0]]
for i in range(Total):
    point=np.matmul(Rotation,point)
    Points.append(point)
Points=np.array(Points)
Points=np.transpose(Points)
x,y=Points
plt.plot(x,y)
plt.savefig("NumpyCircle.eps")
plt.close()


