import pandas as pd 

data = {'이름': ['Kim','Park','Lee','Ho'],
        '국어': [90,58,88,100],
        '영어': [100,60,80,70],
        '수학': [55,65,76,88],
}

df = pd.DataFrame(data)
#데이터 프레임 출력
print(df)
#학생 이름만 추출해서 출력
sr_name = df['이름']
print(sr_name, end='\n\n')
#Park 성적만 출력
print(df.loc[df['이름']== 'Park'], end='\n\n')

#'Ho'학생의 수학점수를 90점으로 수정
df.loc[df['이름']== 'Ho','수학']=90
print(df,end='\n\n')
#새로 추가
df[3]=['Oh',100,70,80]
print(df,end='\n\n')
#'Lee'학생의 성적 삭제
df = df.drop([2],axis=0)
print(df,end='\n\n')
