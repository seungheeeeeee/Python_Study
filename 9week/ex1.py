#학생 수 입력 받아 학생의 수만큼 점수를 입력 받은 후 총점,평균을 계산해서 출력
def printResult(score,total):
    n=len(score)
    print(total)
    print(score)
    print(total/n)


score = []
n = int(input("학생 수:"))

total = 0

for i in range(0,n):
    jumsu=int(input("[%d]영어시험 성적:"% (i+1))) #점수 입력
    total += jumsu #입력받은 수 누적으로 저장, 총점
    score.append(jumsu)

# print 부분 함수로 변경해주기
#print("score=",score)
#print("total=",total)
#print("avg=",total/n)
printResult(score,total) #호출
