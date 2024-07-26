import math
numero = float(input())

while numero < 0:
    print("ERROR,debe ser >=0")
    numero = float(input())
    
i=float(input())
while i <= 0:
    print("ERROR,debe ser >0")
    i = float(input())
raiz = numero ** (1/i)

print(f"{raiz:.3f}")
