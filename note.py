'''
rank	attendance	result
[3, 7, 2, 5, 4, 6, 1]	[false, true, true, true, true, false, false]	20403
[1, 2, 3]	[true, true, true]	102
[6, 1, 5, 2, 3, 4]	[true, false, true, false, false, true]	50200

1   2   3   4   5   6
f   f   f   t   t   t
1   4   4   5   2   0

 10000 × a + 100 × b + c

[1 : (f, 1) 2 : (f : 2)
'''

rank, attendance = [6, 1, 5, 2, 3, 4], [True, False, True, False, False, True]
dic = {}
lst = []
for i, v in enumerate(rank) :
    dic[v] = (attendance[i], i)
lst = [dic[v][1] for v in sorted(dic) if dic[v][0]]
answer = 10000 * lst[0] + 100 * lst[1] + lst[2]
print(answer)



        









