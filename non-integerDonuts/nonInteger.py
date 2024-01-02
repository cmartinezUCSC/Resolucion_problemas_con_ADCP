N = int(input())
total = int(input().split(".")[1]) #volver el input en un numero 
contador  = 0
for i in range(N):
    total += int(input().split(".")[1])
    if (total%100 == 0):
        total = 0
    else:
        contador +=1
print(contador)
