import sys
sys.stdin = open('input.txt', 'rt')
'''
2
2 1 3

1       : [1]
2 3     : [0][2]
====
3
1 6 4 3 5 2 7

3        : [3]
6 2      : [1][5]
1 4 5 7  : [0][2][4][6]

'''

N = int(input())
lst = list(input().split())
answer = [[] for _ in range(N)]

def in_order(lst, depth) :
    mid = len(lst)//2
    answer[depth].append(lst[mid])
    if len(lst) == 1 : return
    in_order(lst[:mid], depth+1)
    in_order(lst[mid+1:], depth+1)

in_order(lst, 0)

for i in answer :
    print(*i)




