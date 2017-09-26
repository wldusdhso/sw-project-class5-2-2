#
n = int(input("Enter n: "))
m = int(input("Enter m: "))


def factorial(x):
    fac = 1
    for i in range(1, x + 1):
        fac *= i
    return fac

print(factorial(n), factorial(m))

def com(n,m):
    return factorial(n) / (factorial(m) * factorial(n - m))

print("C(n,m) = ",int(com(n,m)))



