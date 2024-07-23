N = int(input())

total = int(input().split(".")[1])

t = 0

for i in range(N):
    deposito = int(input().split("."[1]))
    total += deposito
    
    if total % 100 == 0:
        total=0
    else:
        t += 1

print(t)
# no puedo generar los casos