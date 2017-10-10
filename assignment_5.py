import time

#재귀
def fibo(nbr):
    if nbr <= 1:
        return nbr
    return fibo(nbr - 1) + fibo(nbr - 2)


#반복
def iterfibo(nbr):
    answer = [0,1]

    for i in range(2,nbr+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-1]

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