'''
[1, 4, 2, 5, 3]	[1, 2, 3]
'''
arr = [1, 4, 2, 5, 3]

stk = []
'''
for i in range(len(arr)):
    while stk and stk[-1] >= arr[i]:
        stk.pop()
    stk.append(arr[i])
'''

for i in range(len(arr)) :
    while stk and stk[-1] >= arr[i] :
        stk.pop()
    stk.append(arr[i])