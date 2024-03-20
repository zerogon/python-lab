'''

[0, 1, 2, 4, 3]	[[0, 4, 2],[0, 3, 2],[0, 2, 2]]	[3, 4, -1]
'''
arr, queries = [0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]]	
answer = []
tmp = []

for a, b, c in queries :
    for i in arr[a:b+1] :
        if i > c :
            tmp.append(i)
    if len(tmp)== 0 : tmp = [-1]
    answer.append(min(tmp))
    tmp = []

print(answer)

    #for a,b in queries:
     #   arr[a],arr[b]=arr[b],arr[a]








    
