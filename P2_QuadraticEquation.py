import math


a=float(input("the x^2 coefficient:  "))
b=float(input("the x coefficient:  "))
c=float(input("the constant:  "))
# we need to condsider a=0 at first, then the equation becomes linear and only has one real root.

#just 1 case, use a sigle if
#4 spaces after if
if a==0:
    exit("a cannot be 0")
#exit means the program stops

#now comes the non-trivial part.

Delta=math.pow(b,2)-4*a*c

if Delta>0:
    r1=(-b+math.pow(Delta,1/2))/(2*a)
    r2=(-b-math.pow(Delta,1/2))/(2*a)
    print("2 real roots:"+str(r1)+" and "+str(r2))
    #    print("2 complex roots:"+str(r1)+" and "+str(r2))
elif  Delta<0:
    imagine=complex(0,math.pow(-Delta,1/2))
    r1=(-b+imagine)/(2*a)
    r2=(-b-imagine)/(2*a)
    print("2 complex roots:"+str(r1)+" and "+str(r2)) 
else:
    r=-b/(2*a)
    print("repeated root "+str(r))    


