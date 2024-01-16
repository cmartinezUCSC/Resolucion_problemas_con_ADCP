L,R = [int(i) for i in input().split(" ")] #recogemos los dos elementos
resp = [] 
for i in range(L,R+1): #R+1 para que alcance a R 
    aux = 1 #creamos una variable auxiliar
    for j in str(i): #tratamos al numero que evaluamos como un string para poder separarlo elemento a elemento  
        aux = aux*int(j) #realizamos uno a uno el estilo digital
    if aux == 0: #si en algun momento aux da 0 cancelamos de inmediato porque es el numero mas pequeño que va a haber nunca 
        break
    resp.append(aux) #si no hay ningun 0 entonces agregamos todo esto a un arreglo de respuestas
resp.sort() #ordenamos las opciones posibles 
print(resp[0]) #y simplemente imprimimos la primera porque sera la mas pequeña