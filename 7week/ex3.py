#함수없는 버전

number=int(input("숫자를 입력하세요"))

result =True #결과저장
for i in range(2,number): #2부터 number-1까지
    if number%i==0:
        result=False

print(result)


#함수 버전
def check_prime_num(x):
    for i in range(2,x):
        if x%i==0:
            return False
        return True        

number = int(input("숫자를 입력하세요"))
result=check_prime_num(number)
print(result)
        

