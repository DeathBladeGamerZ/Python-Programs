def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def print_primes(m, n):
    for i in range(m, n + 1):
        if is_prime(i):
            print(i, end=" ")

m = int(input("Enter lower limit (m): "))
n = int(input("Enter upper limit (n): "))
print("Prime numbers between", m, "and", n, "are:")
print_primes(m, n)