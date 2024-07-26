n = int(input())
order = input()
custom = input()


# como en este ejercicio nos pide replicar una imagen multiples veces podemos poner las imagenes como funciones para hacer el codigo mas legible
def LoM(aux):  #cabe destacar, el motivo por el agregamos una variable auxiliar es por como funciona python, python no deja que las funciones mas pequeñas modifiquen elementos de funciones mayores por eso no podemos modificar directamente una variable global 
    print("."+(aux[0])+"."+(aux[1])+"...."+(aux[2]))
    print(".."+(aux[0])+"....."+(aux[2]))
    print("."+(aux[1])+"."+(aux[0])+"...."+(aux[2]))
    print((aux[1])+"..."+(aux[0])+"..."+(aux[2]))
    aux = aux[1] + aux[0] + aux[2]


def RoM(aux):
    print(aux[0]+"...."+(aux[1])+"."+(aux[2])+".")
    print(aux[0]+"....."+(aux[2])+"..")
    print(aux[0]+"...."+(aux[2])+"."+(aux[1])+".")
    print(aux[0]+"..."+(aux[2])+"..."+(aux[1]))
    aux = aux[0] + aux[2] + aux[1]


print(custom[0] + "..."+ custom[1] + "..." + custom[2]) #por que el ejercicio lo pide primero imprimimos 1 linea para que quede todo 
if order == "right-over-middle": #preguntamos si se dirigira 
    for i in range(n): #parte hacia la derecha
        if i%2 == 0:
            RoM(custom)
        else:
            LoM(custom)
elif order == "left-over-middle":
    for i in range(n): #parte hacia la izquierda
        if i%2 == 0:
            LoM(custom)
        else:
            RoM(custom)
else: #si no es ninguna de las palabras elegibles no hace nada 
    print("wrong words")
    