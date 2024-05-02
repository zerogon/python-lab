'''

[1, 1, 1, 2, 3, 4, 5]	5	[6, 6]
    [(0,3), (3,4), (6,6)]

[2, 2, 2, 2, 2]	        6	[0, 2]
    [(0,2), (1,3), (2,4)]
'''
sequence, k = [1, 1, 1, 2, 3, 4, 5], 5
answer = []
l = 0
r = 0
sum = 0
'''
sequence	             k	result
[1, 2, 3, 4, 5]     	7	[2, 3]
[1, 1, 1, 2, 3, 4, 5]   5
[2, 2, 2, 2, 2]	        6	[0, 2]
'''
st = set()
while l != len(sequence) :
    sum = sequence[l]
    r = l
    if sum == k :
        
    #elif sum < k :
