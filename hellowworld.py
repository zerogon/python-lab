
'''
[1, 2, 3, 100, 99, 98]	3	[3, 6, 9, 300, 297, 294]
[1, 2, 3, 100, 99, 98]	2	[3, 4, 5, 102, 101, 100]
'''
arr = [1, 2, 3, 100, 99, 98]
answer = list(range(len(arr)))
k = 3

for i in range(len(arr)) :
    if k % 2 == 0 :
        answer[i] = arr[i] + 2
    else :
        answer[i] = arr[i] * 3

print(answer)        