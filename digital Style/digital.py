L,R = [int(i) for i in input().split(" ")]
resp = []
for i in range(L,R+1):
    aux = 1
    for j in str(i):
        aux = aux*int(j)
    if aux == 0:
        break
    resp.append(aux)
resp.sort()
print(resp[0])