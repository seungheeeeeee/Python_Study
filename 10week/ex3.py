import pandas as pd

col_names = ['과목번호', '과목명', '강의실', '시간수']
list1 = list([
    ['C1', '인공지능개론', 'R1', 3],
    ['C2', '웃음치료', 'R2', 2],
    ['C3', '경영학', 'R3', 3],
    ['C4', '3D디자인', 'R4', 4],
    ['C5', '스포츠경영', 'R2', 2],
    ['C6', '예술의 세계', 'R3', 1],
])

df = pd.DataFrame(list1, columns=col_names)
print(df)
print(df.head(3))# 데이터 프레임을 앞에서 3개 행만 출력

sr_name = df['과목명'] #열 추출
print(sr_name, end='\n\n')

sr_one = df.loc[2] # 행 추출
print(sr_one, end='\n\n')

cell_name = df.loc[2]['강의실'] #셀 추출
print(cell_name, end='\n\n')

df.to_csv("lecture.csv", header=True, index=False) # lecture.csv 파일로 저장
