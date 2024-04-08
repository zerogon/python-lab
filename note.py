'''
arr 	k	 result
[0, 1, 1, 2, 2, 3]	3	[0, 1, 2]
[0, 1, 1, 1, 1]	4	[0, 1, -1, -1]
'''
arr , k =[0, 1, 1, 2, 2, 3]	,3
# arr 의 값을 순서대로 넣는다.
answer = []
for i in arr :
    if answer.count(i) == 0 :
        answer.append(i)
    
print(answer)

# 중복된 값은 제외한다.

# 넣어진 값의 크기가 k개가 됐을 경우 리턴.

# 최종값이 k보다 작은 경우 -1로 채운다.