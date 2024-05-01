def sum_int(a,b,c):
    return a * (1+b)**c


p = 30000000
r = 0.051
n= 3

result = sum_int(p,r,n)
print('총액: {0}, 원금:{1}, 이자: {2}'.format(result,p,result-p))
print('총액: %0.2f, 원금:%d, 이자: %0.2f '%(result,p,result-p))


