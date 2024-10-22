num=[]
print("dame una lista de numeros") 
numero=(int)(input("Número: "))
while numero>=0:
    num.append(numero)
    numero=(int)(input("Número: "))
print(num)
print(max(num))
for n in num:
    if n%2==0:
        print(n)

        
 