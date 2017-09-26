
def CombiNation(n, m):
    if m == 1:
        return n
    return CombiNation(n - 1, m - 1) * (n/m)

fstnum = 1
secnum = 1
while fstnum > 0 and secnum > 0:

    fstnum = int(input("Enter n: "))
    secnum = int(input("Enter m: "))

    print("C(%d,%d) =" %(fstnum,secnum),int(CombiNation(fstnum,secnum)))









