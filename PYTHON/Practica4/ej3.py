cadenas = ["hola", "mundo", "mundo", "programación", "inteligencia artificial"]
cad=input("dame una cadena ")
try : 
    print(cadenas.index(cad)+1)
  
except:
    print("no se ha encontrado la cadena")

cant=str(cadenas.count(cad))
print("numero de veces encontrada "+cant)

print(cadenas)
cadRE=input("dame una palabra de la cadena a remplazar ")
cadRT=input("dame la palbra por la que se reemplaza")

if cadRE==cadRT:
    print("Error es la misma cadena")
    exit

try : 
    while str(cadenas.count(cadRE))!=0:
        cadenas[cadenas.index(cadRE)]=cadRT
        
    
except:
    print("no se ha encontrado la cadena en la list")

print(cadenas)