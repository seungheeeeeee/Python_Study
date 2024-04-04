dict_1 = {'name': '홍길동','birth': 1990, 'addr': 'KR'}
print(dict_1)
print(dict_1['birth']) #접근 할 때 key값으로 !
# 추가, 배열로 넣을 수 있음, 또 다른 딕셔너리도 넣을 수 있음
dict_1['weight'] = 60.5 
dict_1['family'] = ['아빠','엄마','여동생']
print(dict_1)

dict_1.update({'weight':67.8, 'hobby':['게임','독서']}) #통합, 딕셔너리 형태, 두개 합쳐진다.
print(dict_1)

dict_1['hobby']=['축구','등산'] # hobby값 있으면수정
print(dict_1)

del dict_1['weight'] #삭제
del dict_1['birth']
del dict_1['addr']
print(dict_1)
