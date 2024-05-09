#pandas import 해주기
import pandas as pd

list1 = list(
    [
        ["한빛","남자","20","180"],
        ["한결","남자","21","177"],
        ["한라","여자","20","160"],
    ]
)

col_names = ["이름","성별","나이","키"] #컬럼 이름 붙이기 , 인덱스는 자동으로 붙여짐
df = pd.DataFrame(list1, columns=col_names) 
print(df)

df.to_csv("file.csv", header=True, index=False) #데이터 프레임을 csv로 저장 