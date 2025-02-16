#lcm
n1=(input())
n2=(input())
try:
    n1=int(n1)
    n2=int(n2)
except ValueError:
    try :
        n1=float(n1)
        n2=float(n2)
        print("invalid")
        raise SystemExit("Exiting the program.")

    except ValueError:
        try:
            n1=complex(n1)
            n2=complex(n2)
            print("invalid")
            raise SystemExit("Exiting the program.")

        except ValueError:
            print("invalid")
            raise SystemExit("Exiting the program.")
# try:
#     n2=int(n2)
    
# except ValueError:
#     try :
#         n2=float(n2)
#         print("invalid")
#         raise SystemExit("Exiting the program.")

#     except ValueError:
#         try:
#             n2=complex(n2)
#             print("invalid")
#             raise SystemExit("Exiting the program.")

#         except ValueError:
#             print("invalid")
#             raise SystemExit("Exiting the program.")
else:
    n1=int(n1)
    n2=int(n2)
    original_n1=n1
    original_n2=n2
    if(n1>n2):
        while(n1%n2 != 0):
            temp=n2
            n2=n1%n2
            n1=temp
        gcd=n2
        lcm=(original_n1*original_n2)/gcd
        print(int(lcm)) 
    elif(n2>n1):
        while(n2%n1 != 0):
            temp=n1
            n1=n2%n1
            n2=temp
        gcd=n1
        lcm=(original_n1*original_n2)/gcd
        print(int(lcm)) 
