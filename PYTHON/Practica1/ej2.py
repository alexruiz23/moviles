import math
print("dame el radio en metros")    
radio=input()
int_radio=int(radio)
print(type(int_radio))
area=2*int_radio*math.pi
print(math.trunc(area))
