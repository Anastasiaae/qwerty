import math
x=int(input())
t=int(input())
z=(9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-abs(math.sin(t)))*math.exp(x)
print(round(z,2)) 