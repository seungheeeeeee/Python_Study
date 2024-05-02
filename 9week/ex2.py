#모듈을 사용하는 파일
import md
print("10~20사이의 소수:")
for j in range(10,20) :
    if md.isPrime(j) :
        print(j)