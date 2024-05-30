#데이터 정제 실습: 결측치 처리
import pandas as pd 

air = pd.read_csv('air.csv')

print("1***************************")
print(air, end="\n\n")
air.info() # 컬럼별 non-null 데이터 있는 수

print("2***************************")
print(air.isnull().sum(), end="\n\n") #결측치의 수
#삭제
print("3***************************")
air_d = air.dropna(axis=0)
print(air_d, end="\n\n")

print("4***************************")
air_d2 = air.dropna(axis=1)
print(air_d2, end="\n\n")
# 대체
print("5***************************")
air_m1 = air.fillna(0)
print(air_m1, end="\n\n")

print("6***************************")
mean = air['PM10'].mean()
air_m2 = air['PM10'].fillna(mean)
print(air_m2, end="\n\n")
