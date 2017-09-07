
answer = 0
while answer != -1:


    answer = int(input("Enter a number: "))

    n = answer
    f = 1
    if answer == -1:
        break
    elif answer <=-2:
        print("No Answer")
    while n != 1:
        f = f * n
        n = n-1
    print(f)