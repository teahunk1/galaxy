#print("0보다 크고 99보다 작은 수를 입력")  이준형 답
sum=int(input())
cycle=0
b=0


if  sum==0:
    print("1")
else:
    temp=(sum//10+sum%10)%10+10*(sum%10)
    cycle+=1
    while temp!=sum:
        temp=(temp//10+temp%10)%10+10*(temp%10)
        cycle=cycle+1
    print(str(cycle))

