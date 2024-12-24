from sympy import isprime

num = int(input("Enter a number: "))
if isprime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

