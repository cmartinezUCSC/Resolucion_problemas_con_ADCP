def main():
    a, b, c = 0, 0, 0
    
while True:
    try:
        a, b, c = map(int, input("Edades de los 3 hermanos?(separados por un espacio):").split())
            
        if a > 0 and b > 0 and c > 0:
            break
        else:
            print("ERROR, Todas las edades deben ser no negativas y distintas de 0.")
    except ValueError:
        print("ERROR, entrada no valida. Ingrese numeros enteros.")
            
if( b < a < c) or (c < a < b):
    medio=a
else:
    if( a < b < c) or (c < b < a):
        medio=b
    else:
        if( a < c < b) or ( b< c < a):
            medio = c

print ("El hijo del medio es {}".format(medio))
        
if __name__ == "__main__":
    main()