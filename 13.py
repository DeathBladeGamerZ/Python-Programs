def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

num = int(input("Enter a number: "))
print("Factorial (Recursive):", factorial_rec(num))