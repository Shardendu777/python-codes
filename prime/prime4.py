def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

while True:
    n=(input("Enter a number: "))
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
    if is_prime(n):
        print("Prime Number")
        break