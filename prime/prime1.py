#import sys
number=int(input("how many times you want to enter number:"))
for i in range(number):
    n=input()
    try:
        n = int(n)
    except ValueError:
        try:
            n = float(n)
            print("invalid")
            continue
        except ValueError:
            try:
                n = complex(n)
                print("invalid")
                continue
            except ValueError:
                print("invalid")
                continue
    if(n==1):
        print("invalid")
        continue
    elif(n<=0):
        print("invalid")
        continue
    else:
        i=2
        while(i<n):
            if(n%i==0):
                print("not prime")
                break
            i+=1
        else:
            print("prime")
            