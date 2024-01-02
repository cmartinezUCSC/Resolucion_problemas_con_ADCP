n,k,x = [int(i) for i in input().split()]
chests = []

for i in range(n):
    chests.append(input().split(" "))

print(chests)
print(chests[1][3])
for i in range(len(chests)):
    print(str(i) + ": ")
    for j in chests[i]:
        print("\t"+ str(j))