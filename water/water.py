T = int(input())

for j in range(T):
    n,c = [int(i) for i in input().split(" ")];
    C_usar = c;
    dep_usa = 1
    Cn = [int(i) for i in input().split(" ")]
    for i in Cn:
        C_usar = C_usar - i;
        if C_usar <= 0:
            dep_usa+=1;
            C_usar = c;
    print(dep_usa)    