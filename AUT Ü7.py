import math

vrz=9
frz=75
k=18/3
D=0.35682

x=1/(4*(vrz/k)**2)



ohmega=(2*math.pi*frz)/(math.sqrt(1-2*D**2))

c1=(2*D)/(ohmega)
c2=1/(ohmega**2)

print(c1)
print(c2)