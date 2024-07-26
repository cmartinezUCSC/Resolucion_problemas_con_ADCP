S = input()

nom = ["Bob", "Alice", "Cindy"]

resp = ""

if len(S) == 3:
    for i in range(3):
        if S[i] == nom[0][i]:
            resp = resp + S[i]
        elif S[i] == ".":
            resp = resp + nom[0][i]
        else:
            resp = "algo salio mal"
            break

elif S == ".....":
    resp = "NO SE PUEDE DETERMINAR"
else:
    for i in range(5):
        if S[i] == nom[1][i]:
            resp = resp + S[i]
        elif S[i] == ".":
            resp = resp + nom[1][i]
        else:
            resp = "algo salio mal"
            break
    
    if resp != nom[1]:
        resp = ""
        
        for i in range(5):
            if S[i] == nom[2][i]:
                resp = resp + S[i]
            elif S[i] == ".":
                resp = resp + nom[2][i]
            else:
                resp = "algo salio mal"
                break

print(resp)