def sum_int(a,b,c):
    return a * (1+b)**c


p = 30000000
r = 0.051
n= 3

result = sum_int(p,r,n)
print(f'{p} * {(1+r)}**{n} = {result}')
