import sys
sys.stdin = open('input.txt', 'rt')
class Node:
    def __init__(self, data, left_node, right_node) :
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node) :
    print(node.data, end='')
    if node.left_node != None :
        pre_order(tree[node.left_node])
    if node.right_node != None :
        pre_order(tree[node.right_node])
def in_order(node) :
    if node.left_node != None :
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None :
        in_order(tree[node.right_node])
def post_order(node) :
    if node.left_node != None :
        post_order(tree[node.left_node])
    if node.right_node != None :
        post_order(tree[node.right_node])
    print(node.data, end='')
n = int(input())
tree = {}

for i in range(n) :
    data, left_node, right_node = input().split()
    if left_node == "." :
        left_node = None
    if right_node == "." :
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])


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
'''
3
1 6 4 3 5 2 7
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






        