
'''
'''
arr, idx = [0, 0, 0, 1]	,1	
answer = 0

for i, v in enumerate(arr) :
    if i >= idx :
        if v == 1 :
            answer = i



print(answer)
