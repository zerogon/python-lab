'''

genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.


classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.
'''
genres ,	plays =["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]
# 4 3 1 0 2
# 체크포인트
# 1. 장르별로 재생횟수가 큰 순서 필요
# 1-1 장르에서 재생횟수가 큰 순서 필요
# 1-2 장르에서 같을 경우 고유번호 낮은
# 1-3 장르에서 2개 초과해서 추가할수 없음

dic1 = {}
dic2 = {}
'''
for i in range(len(genres)) :
    dic1[genres[i]] = dic1.get(genres[i],[])+[plays[i]]
print(dic1)
'''
for i, v in enumerate(genres) :
    if v not in dic1.keys() :
        dic1[v] = plays[i]
    else :
        dic1[v] += plays[i]

print(dic1)
for i, v in enumerate(genres) :
    if v not in dic2.keys() :
        dic2[v] = [(i, plays[i])]
    else :
        dic2[v] += [(i, plays[i])]
print(dic2)
sorted_keys = sorted(dic1,key= lambda x : dic1[x], reverse=True)
#s2 = sorted(dic2,key= lambda x : dic2[x][1], reverse=True)









