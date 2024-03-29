
print("수를 입력해 주세요:")
a = int (input()) #int 타입 정해주기
i=1
num=0 # 변수 선정
if a <=9:
    for i in range(0,10):
        num = a*i # num 변수 선정하지 않고 쓰면 무한루프 발생 
        print(f"{a}X{i}={num}")
else:print("1~9까지의 수를 입력해")
    