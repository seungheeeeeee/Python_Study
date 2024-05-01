#서브로직
def printArguments(x, y, z):
    print("x=%d, y=%d, z=%d" % (x, y, z))
    sum = x + y + z
    print("x+y+z=%d" % sum)
#메인 로직
printArguments(10, 20, 30)  #순서상관 없이 이름으로 매칭 가능
printArguments(y=100, z=200, x=300)
printArguments(z=2000, y=1000, x=3000)