#i값 설정
i = 1

#while문 이용하여 i를 입력값에 따라 계속 바꾸어줌
while i != -1 :
    i =  int(input("Enter a number : "))
    if i == -1: break #if문 이용하여 i가 -1일 때 반복문 멈춤 
    total = 1 #total값 설정
    #for문 이용하여 total을 팩토리얼 계산에 맞게 계속 곱해줌
    for a in range(i,0,-1):
        total = total*a
    print(i, "! = ", total) #최종 값 프린트

