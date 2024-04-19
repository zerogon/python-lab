'''

순열 https://www.acmicpc.net/problem/10972

'''
# 트리
import sys
sys.stdin = open('input.txt', 'rt')


class Node :
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def in_order(node) :
    if node.left_node != None :
        in_order(node.left_node)
    print(node.data, end= ' ')
    if node.right_node != None :
        in_order(node.right_node)

def pre_order(node) :
    print(node.data, end= ' ')
    if node.left_node != None :
        pre_order(dic[node.left_node])
    if node.right_node != None :
        pre_order(dic[node.right_node])

def post_order(node) :
    if node.left_node != None :
        post_order(node.left_node)
    if node.right_node != None :
        post_order(node.right_node)
    print(node.data, end= ' ')

N  =  int(input())
dic = {}
for _ in range(N) :
    data, a, b = input().split()
    if a == '.' : a = None
    if b == '.' : b = None
    dic[data] = Node(data, a, b)

pre_order(dic["A"])













        