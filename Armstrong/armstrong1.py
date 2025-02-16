#armstrong
import sys
n=input()
try:
    n=int(n)
    
except ValueError: #if we don't write the error it will print invalid it more than on time 
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

original_n=n
count=0
arm=0
while(n>0):
    n=n//10
    count=count+1
    
n=original_n

while(n>0):
    t=n%10
    arm+=t**count
    n=n//10
if(arm==original_n):
    print("armstrong")
else:
    print("not armstrong")
