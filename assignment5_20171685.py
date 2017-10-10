import time
import random

def fibo(n):
        if n <= 1:
                return n
        return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    answer_list = [1]
    for i in range(0,n-1):
        if i ==0:
            answer_list.append(1)
        else:
            Add = answer_list[i] + answer_list[i-1]
            answer_list.append(Add)
    return answer_list[n-1]

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))




