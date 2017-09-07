num = int(input("Enter a number : "))
n = 1
for i in range(1, num+1):
    if i != -1:
        n = n*i
    elif i == -1:
        break
print(num, "! = ", n)