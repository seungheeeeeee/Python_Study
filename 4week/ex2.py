while True: #반복하여 동작
    print("음료목록 1.오렌지주스(100원),2.커피(200원),3.콜라(300원)")
    coin=int(input("동전을 넣으세요:"))
    drink=int(input("음료를 고르세요:"))
    
    
    if drink==1: #들여쓰기 주의 while 적용
        if coin >=100:#동전 비교
            remain = coin-100#차액
            print("오렌지 주스가 곧 제공됩니다")
            print("거스름돈은{}원입니다.".format(remain))
        else :
            print("잔액이 부족합니다.")
    if drink==2:
        if coin >=200:#동전 비교
            remain = coin-200#차액
            print("커피가 곧 제공됩니다")
            print("거스름돈은{}원입니다.".format(remain))
        else :
            print("잔액이 부족합니다.")
    if drink==3:
        if coin >=300:#동전 비교
            remain = coin-300#차액
            print("콜라가 곧 제공됩니다")
            print("거스름돈은{}원입니다.".format(remain))
        else :
            print("잔액이 부족합니다.")
else :
    print("없는메뉴입니다")

    coin = 0
        




    
    



