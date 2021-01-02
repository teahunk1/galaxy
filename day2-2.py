#파이썬은 반복문은 for 문과 while 문
#while 문 

a=int(input()) #while 뒤에는 판별(참,거짓이 구분가능)이 가능한 조건이 와야됨
b=0
#*소환

#print("입력한 수는"+ str(a))
#while b<a+1:
#   print("*"*b)
#    b=b+1
#b=b-1
#while b>0:
#    print("*"*b)
#    b=b-1

# while True:
#    if b <= a and check:
#        print("*"*b)
#        b+=1
#        if b == a:
#            check = False
#    else:
#        print("*"*b)
#        b-=1
#        if b == 0:
#            break """
#입력한 숫자 이하의 모든 홀수를 출력

while b<=a:
    if b%2==0:
        print(b)
    b=b+1


