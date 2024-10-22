def filtras_palabras():
    l=["hola","h","ho","hol","holas"]
    
    x=int(input("dame un numero"))
    
    for i in l :
     if x ==len(i):
         print("Tiene los mismos caracteres "+i)
   
filtras_palabras()