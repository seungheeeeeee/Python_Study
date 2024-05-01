import turtle as t

t.shape("turtle")

t.forward(100)  #거북이가 100만큼 앞으로 이동
t.left(120)     #거북이가 왼쪽으로 120도 회전
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.circle(50)    #반지름이 50인 원을 그린다.

t.color("red")  #펜 색상을 빨간색으로 변경
t.pensize(3)    #펜 굵기를 3으로 변경

for i in range(4) :     #아래 로직을 4번 반복
    t.forward(100)      #거북이가 100만큼 앞으로 이동
    t.left(90)          #거북이가 왼쪽으로 90도 회전0

t.mainloop()

