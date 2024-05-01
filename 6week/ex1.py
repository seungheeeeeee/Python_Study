def sum_int(a,b):           #서브로직
        return a+b

num1 = 10                   #메인로직
num2 = 20

result = sum_int(num1,num2) #함수 호출하는 부분 
print(f'{num1} + {num2} = {result}')