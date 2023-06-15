import math

volume=input("please show me the volume in m^2: ")

#update the variable volume, change into float format
#float format is math-friendly
#Otherwise, the string cannot undergo the following math-operations
volume=float(volume)

#unit conversion 
#redius cube
radius3=(3*volume)/(4*math.pi)

#take the 3rd root to get radius
radius=math.pow(radius3,1.0/3)

#find area using formular
area=4*math.pi*math.pow(radius,2)

print("the radius of the sphere in m is : "+str(radius))
print("the surface area of the sphere in m^2 is : "+str(area))

