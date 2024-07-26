n= -1
while n <= 0:
    n=int(input("Ingrese un entero positivo : "))
    if n <= 0:
        print("Debe ser positivo!")
    

cubo = 0
impar = (n*(n-1))+1

for i in range (n):
    cubo += impar
    impar += 2
print (f"El cubo es : ({cubo})")