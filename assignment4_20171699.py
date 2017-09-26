n = int(input("Enter n"))
m = int(input('Enter m'))

def combination(m,n):
    com = factorial(n)/(factorial(m)*factorial(n-m))
    return com


def factorial(m):
    fac = 1
    for i in range(1, m+1):
        fac *= i
    return fac

print(combination(m,n))



