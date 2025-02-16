import sys
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
if(n==1):
    print("invalid")
elif(n<=0):
    print("invalid")
else:
    i=2
    while(i<n):
        if(n%i==0):
            print("not prime")
            sys.exit()
        i+=1
    else:
        print("prime")