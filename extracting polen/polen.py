N,K = [int(i) for i in input().split(" ")] 
flores = input().split(" ")

for i in range(K): # con esta funcion haremos avanzar a todas las 
    recolecta = 0
    for j in flores[0]: #esto separa el numero en sus elementos independientes
        recolecta += int(j) #recolectamos el polen 
    flores[0] = str(int(flores[0]) - recolecta) #y lo quitamos del polen total de la flor
    if flores[0] == '0': #si la flor se quedara vacia la eliminamos de lista de flores
        flores.remove('0')  
    

#finalmente llegamos al turno de gertrude asi que replicamos el proceso una ultima vez y lo imprimimos    
recolecta = 0
for j in flores[0]:
    recolecta += int(j)
print(recolecta)