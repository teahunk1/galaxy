print("hello world")
#조건문 if랑 else 
a=int(input())
print("입력한 수는 "+str(a))
if a%2==0: #4칸 띄우기
    print("짝수입니다..")
elif a%2==1:  #파이선에 있는 다른 조건문, if가 미처 잡지못한 조건으로 
    print("홀수입니다.")

else: 
    print("1이 아닙니다.")  
    print("바보")


