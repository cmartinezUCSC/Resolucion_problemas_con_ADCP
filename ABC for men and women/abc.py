S = input() 
nom = ["Bob","Alice","Cindy"] #anotamos los tres nombres para tener una gestion mas simple del 
resp = "" #dejamos esto como un string vacio para usarlo mas adelante

if len(S) == 3:   #aca es donde comienzas las preguntas, primero vemos si la palabra puede ser bob o no puesto que es el unico nombre con 3 caracteres de largo
    for i in range(3): 
        if S[i] == nom[0][i]: #si la letra en cuestion coincide con la de la misma posicion decimos que esta bien y en resp anotamos esa letra 
            resp = resp + S[i]
        elif S[i] == ".": #si la letra fuera un punto asumimos que es la letra del nombre que le corresponde 
            resp = resp + nom[0][i]
        else: # si ninguna de estas posibilidades se cumple asumiremos que algo salio mal y diremos que algo salio mal y terminaremos el programa 
            resp = "somethin wrong"
            break
elif S == ".....": #por otro lado si son todos puntos y son cinco caracteres diremos que no se puede determinar 
    resp = "CAN'T TELL"
else: #si ese no fuera el caso y ubiera algunas letras podemos replicar lo que hicimos con bob pero con los dos nombres que faltan por verificar.
    for i in range(5):
        if S[i] == nom[1][i]:
            resp = resp + S[i]
        elif S[i] == ".":
            resp = resp + nom[1][i]
        else:
            resp = "somethin wrong"
            break
    if resp != nom[1]:
        resp = ""
        for i in range(5):
            if S[i] == nom[2][i]:
                resp = resp + S[i]
            elif S[i] == ".":
                resp = resp + nom[2][i]
            else:
                resp = "somethin wrong"
                break    

print(resp)