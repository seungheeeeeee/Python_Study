import pandas as pd 

data = {'이름': ['Kim','Park','Lee','Ho'],
        '국어': [90,58,88,100],
        '영어': [100,60,80,70],
        '수학': [55,65,76,88],
}

df = pd.DataFrame(data)

print(df)

sr_name = df['이름']
print(sr_name, end='\n\n')

print(df.loc[df['이름']== 'Park'], end='\n\n')


df.loc[df['이름']== 'Ho','수학']=90
print(df,end='\n\n')

df[3]=['Oh',100,70,80]
print(df,end='\n\n')

df = df.drop([2],axis=0)
print(df,end='\n\n')
