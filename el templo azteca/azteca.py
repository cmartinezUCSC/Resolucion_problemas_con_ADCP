def orden(a):
    return len(a)

n = int(input()) #tamaño de la piramide 
piramide = []; # un arreglo donde meteremos todos los segmentos de la piramide como lleguen 

for i in range(n): #recibimos las piezas y las separamos en torno a los espacios, esto para saber que tamaño tiene cada pieza
    piramide.append(input().split(" "));

piramide.sort(key=orden)  #ordena todo de forma ascendente, la funcion orden le indica que lo haga en torno al tamaño del arreglo de la piramide

for i in range(n):
    print(piramide[i])


