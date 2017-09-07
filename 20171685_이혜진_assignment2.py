n= int(input("Enter a number: "))
while (1):
    A= 1
    if n>0:
        for i in range(1,n+1):
            A = A*i
        print("%d! = %d"%(n,A))
    elif n==0:
        print("0! = 1")
    elif n<-1:
        print("no answer")
    elif n==-1:
        break
    n= int(input("Enter a number: "))
    
