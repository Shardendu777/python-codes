n=input()
fac=1
i=1
try:
    n=int(n)
    
except ValueError:
    try :
        n=float(n)
        print("invalid")
        raise SystemExit("Exiting the program.")

    except ValueError:
        try:
            n=complex(n)
            print("invalid")
            raise SystemExit("Exiting the program.")

        except ValueError:
            print("invalid")
            raise SystemExit("Exiting the program.")
if(n<0):
        print("invalid")
else:
    n=int(n)
    if(n==0 or n==1):
        print("1")
    else:
        while(i != n+1):
            fac=fac*i
            i+=1
        print(fac)
        