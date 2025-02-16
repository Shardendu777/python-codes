# Armstrong Number Checker
import sys

n = input("Enter a number: ")

# Validate input: Accept only integers.
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

# Store the original number for comparison later.
original_n = n

# Count the number of digits in the number.
count = 0
temp = n
while temp > 0:
    temp //= 10
    count += 1

# Calculate the Armstrong sum using the counted digits.
arm = 0
temp = n
while temp > 0:
    digit = temp % 10
    arm += digit ** count
    temp //= 10

# Check if the Armstrong sum matches the original number.
if arm == original_n:
    print("armstrong")
else:
    print("not armstrong")
