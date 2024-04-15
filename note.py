'''
clothes	return
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3
'''
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

''

'''
headgear : [1, 2, 3]
eyewear : [1]
face : [1,2]
'''
dic={}
answer = 1
for a, b in clothes :
    if b not in dic.keys() :
        dic[b] = [a]
    else :
        dic[b] += [a]
for k, v in dic.items() :
    answer *= (len(v) + 1)

print(answer)
