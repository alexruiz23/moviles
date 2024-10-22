        
def lista(n,lista):
    for t in lista:
        if t[0]==n:
            return True
    return False

nombres=list()
l_frecuencias=list()

while True:
    nombre=input("Dame un nombre : ")
    if nombre==-1:
        break;
    nombres.append(nombre)
for i in nombres :
    if lista(i,l_frecuencias):
        continue
    X=nombres.count(i)
    l_frecuencias.append(i,x)
    
print(l_frecuencias)
