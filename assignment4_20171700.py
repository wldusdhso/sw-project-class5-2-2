n = 1
r = 1
def nCr(n, r):
    if r == 0 or n== r:
        return 1
    elif n < r :
        print("Try again")
    else:
        return nCr(n-1, r-1) + nCr(n-1, r)

while True:
    try:
        if r>=0 and n >= 0:
            n = int(input("Enter number(n) : "))
            r = int(input("Enter number(r) : "))
            print(nCr(n, r))

    except:
        break