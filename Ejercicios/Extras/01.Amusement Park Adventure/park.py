N,H = [int(i) for i in input().split(" ")] #por la forma en la que trabaja python tomamos de todas formas ambos datos
alturas = input().split(" ") #pero tomamos todas los siguientes casos y simplemente los separamos para hacerlos arreglos
resp = 0
for i in alturas: #luego recorremos 
    if H > int(i): #y verificamos el tamaño 
        resp+=1

print(resp)