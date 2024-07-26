
T = int (input())

for j in range (T):
    n,c = [int(i) for i in input().split(" ")]
    C_uso = c
    baldes = 1
    
    Cn = [int(i) for i in input().split(" ")]
    for i in Cn:
        C_uso -= i
        if C_uso <= 0:
            baldes += 1
            C_uso = c
            
    print(baldes)