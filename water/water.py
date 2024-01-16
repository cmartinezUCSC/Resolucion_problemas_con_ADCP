T = int(input()) #casos que pide 

for j in range(T):
    n,c = [int(i) for i in input().split(" ")]; #recogemos la cantidad de personas y la cantidad de litros que soportara el tanque
    C_usar = c; # cuantos litros tiene en un momento especifico el tanque 
    dep_usa = 1 #la respuesta a imprimir
    Cn = [int(i) for i in input().split(" ")] #la cantidad de agua que quieren sacar 
    for i in Cn:
        C_usar = C_usar - i; #restamos la cantidad que quiere sacar la persona 
        if C_usar <= 0: # y revisamos si el valor es mayo a 0 y si lo es 
            dep_usa+=1; #contamos el hecho de rellenar el estanque 
            C_usar = c; #y lo volvemos a rellenar
    print(dep_usa)    