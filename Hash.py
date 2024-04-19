'''
https://school.programmers.co.kr/learn/courses/30/lessons/42579
'''
genres ,	plays =["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]

total = {}
gen = {}
answer = []

for i in range(len(genres)) :
    total[genres[i]] = total.get(genres[i], 0) + plays[i]
    gen[genres[i]] = gen.get(genres[i],[]) + [(plays[i],i)]
sorted_total = sorted(total.items(), key= lambda x : x[1], reverse=True)

for i, v in sorted_total :
    print("gen[i]:", gen[i])
    answer += [v for i, v in sorted(gen[i], key= lambda x : x[0],reverse=True)[:2] ]
print(answer)


#딕셔너리 활용
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
dic={}
answer = 1
for a, b in clothes :
    dic[b] = dic.get(b, []) + [a]
