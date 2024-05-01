#서브로직
def localTrade():
    global price    # 메인로직 price를 가져와서 쓸 수 있음
    salePrice = price * 1.2
    print(price, salePrice)
    price = 2000
    salePrice = price * 1.2
    print(price, salePrice)
#메인로직
price = 1000        #전역변수화 시킴. 양쪽으로 쓸 수 있는
localTrade()
print(price)