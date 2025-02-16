a=0
b=1
n=input()
try:
    n = int(n)
except ValueError:
    try:
        n = float(n)
        print("invalid")
        raise SystemExit("Exiting the program.")

    except ValueError:
        try:
            n = complex(n)
            print("invalid")
            raise SystemExit("Exiting the program.")
        except ValueError:
            print("invalid")
            raise SystemExit("Exiting the program.")

else:
    n=int(n)
    if(n==0 or n<0):
        print("invalid")
    elif(n==1):
        print("0")
    elif(n==2):
        print("0 1")
    else:
        print("0\n1")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c)
            