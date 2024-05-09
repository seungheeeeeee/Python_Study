import pandas as pd

df = pd.read_csv("file.csv", sep=',')
print(df, end='\n\n')
print(df.head(2)) # 데이터프레임으로부터 행을 가져옴
print(df.tail(1))

sr_name = df['이름'] #열 추출
print(sr_name, end='\n\n')

sr_two = df.loc[1] # 행 추출
print(sr_two, end='\n\n')

cell_name = df.loc[1]['이름'] #셀 추출
print(cell_name, end='\n\n')
# 표현 다르게
cell_name_name = df.loc[1,'이름'] 
print(cell_name, end='\n\n')