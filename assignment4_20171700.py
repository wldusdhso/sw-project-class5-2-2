n = int(input("Enter number(n) : "))
r = int(input("Enter number(r) : "))
def nCr(n, r):
    if r == 0 or n== r:
        return 1
    elif n < r :
        print("Try again")
    else:
        return int(nCr(n-1, r-1) + nCr(n-1, r))

print(nCr(n, r))