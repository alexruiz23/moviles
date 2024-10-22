
def simbolo():
    print("dame un caracter")
    caracter=input()

    if (caracter>='a') & (caracter<='z'):
        print("es un caracter")
    elif(caracter>='A') & (caracter<='Z'):
            print("es un caracter")
    elif (caracter>='0') & (caracter<='9'):
        print("es un numero")
    else:
        print("es un simbolo")

simbolo()   
     



