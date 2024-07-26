N = int(input())
total = int(input().split(".")[1]) #tomamos la parte decimal del numero que a final de cuentas es lo que nos interesa
contador  = 0
for i in range(N): 
    total += int(input().split(".")[1]) #la sumamos a la pila de ahorros
    if (total%100 == 0): #si esta parte es distinta de 0 significa que el valor en el banco es un valor no entero y deberiamos contarla 
        total = 0 #si es 0 entonces volvemos el valor a 0 para empezar de nuevo
    else:
        contador +=1
print(contador)
