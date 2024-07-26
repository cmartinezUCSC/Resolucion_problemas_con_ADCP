def main():
    p0 = 3
    p1 = 0
    p2 = 2
    
    n = int(input("ingrese n:"))
    if n == 0:
        print(f"({p0})")
    elif n == 1:
        print(f"({p1})")
    elif n == 2:
        print (f"({p2})")
    else:
        perrin = 0
        for i in range (3, n + 1):
            perrin = p1 + p0
            p0 = p1
            p1 = p2
            p2 = perrin
        print(f"({perrin})")

if __name__ == "__main__":
    main()