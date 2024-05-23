import pandas as pd
import mariadb
#DB 연결
conn = mariadb.connect(
    user="user025",
    password="!ai123",
    host="edu.ithows.com",
    port=53306,
    database="edudb"
)
cusor = conn.cursor() #커서 생성
# 검색 부분
cusor.execute('SELECT * FROM city')
results = cusor.fetchall()
for row in results:
    print(row)
#DataFrame으로 결과 변환
df = pd.DataFrame(results)
print(df.head(10), end="\n\n")
# 연결 종료
conn.close()
