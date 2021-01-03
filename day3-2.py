a=int(input())
print("입력받은수는 "+str(a))
for i in range(1,10):    #  0부터 순서대로 range이전까지의 정수를 냄, 
                         #단 원하는 경우 시작숫자를 정할수 있음 
                         #(시작(포함 함),마지막(포함은 안함),간격)
    print(a*i)