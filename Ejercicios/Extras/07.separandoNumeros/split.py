#other = int(other,2)
n = int(input()) #definimos primero el numero que usaremos para nuestro ejercicio
while(n != 0):
    a = 0 #luego definimos las variables para la respuesta 
    b = 0
    bi = format(int(n),'b')
    paso = True
    for i in range(len(bi)): #esta forma si bien parece engorrosa es una forma simple de separar valores binarios
      if (n & (1<<i)) != 0: #con esto verificamos si el valor es 0 o distinto de 0 
            if paso: #en este if iremos intercalando hacia donde va cada 1 y su valor en decimal se ira sumando a la respuesta
                a+=(n&(1<<i))
            else:
                b+=(n&(1<<i))
            paso = not paso #con esto finalmente hacemos que se intercalen a y b

    print(str(a) +" " + str(b))
    n = int(input())