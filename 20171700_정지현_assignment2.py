num = 0
while num != -1:
    num = int(input("Enter a number : "))
    factorial = 1

    if num < 0:
         print("Error")
    elif num == 0:
        print("0! = 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
        print(num, "! = ", factorial)
