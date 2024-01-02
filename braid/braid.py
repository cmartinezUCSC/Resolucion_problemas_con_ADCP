n = int(input())
order = input()
custom = input()

def LoM(aux):
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


print(custom[0] + "..."+ custom[1] + "..." + custom[2])
if order == "right-over-middle":
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
else:
    print("wrong words")
    