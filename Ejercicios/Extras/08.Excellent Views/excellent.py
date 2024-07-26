def dist(n,i):
    return n - i

n = int(input()) #cantidad de edificios en la ciudad
alturas = [int(i) for i in input().split(" ")]  #la altura de estos edificios

posicion = list(range(1,n+1)) #la posicion de cada edificio para poder sacar sus distancias

distancias = [] 

#for que edificio a edificio ira sacando sus distancias correspondientes para ver que tal
for i in posicion:
    aux = []
    for j in posicion:
        aux.append(abs(j-i))    
    distancias.append(aux)



print(alturas)
print(posicion)
print(distancias)