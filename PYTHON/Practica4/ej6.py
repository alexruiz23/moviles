import random


j=random.randint(1,2)
x=input("el primer nombre")
y=input("el segundo nombre")
xlife=100
ylife=100
xataque=random.randint(1,10)  
yataque=random.randint(1,10)

l=[[x,xlife,xataque],[y,ylife,yataque]]

while xlife!=0 | ylife!=0:
    
    if j==x:
        ylife=ylife-xataque
        j=0
    else:
     xlife=xlife-yataque
    if j==0:
     l[ylife]=l[ylife]-l[xataque]   
     l[xlife]=l[xlife]-l[yataque]

print(l)






    
