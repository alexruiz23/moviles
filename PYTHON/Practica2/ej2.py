mes=13
while mes<=0 | mes >12 :
    print("INtroduce un  numero entre 1 y 12")
    mes=int(input())

fecha31=(1,3,5,7,8,10,12)
fecha3o=(4,6,9,11)

if mes in fecha31:   
    print("tiene 31")
elif mes in fecha3o:
    print("tiene 30")
else:
  print("tiene 31")