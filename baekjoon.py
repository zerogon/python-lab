import sys
sys.stdin = open('input.txt', 'rt')
'''
7
1 6
6 3
3 5
4 1
2 4
4 7

'''

N = int(input())
class Node:
    def __init__(self, data, left_node, right_node) :
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def in_order(node) :
    if node.left_node != None :
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None :
        in_order(tree[node.right_node])

tree = {}
for i in range(1, N) :
    data, left_node, right_node = input().split()
    if left_node == "." :
        left_node = None
    if right_node == "." :
        right_node = None
    tree[data] = Node(data, left_node, right_node)

