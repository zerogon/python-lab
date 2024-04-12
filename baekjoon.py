import sys
sys.stdin = open('input.txt', 'rt')
'''
n = input()
lst = []
for _ in range(int(n)) :
    lst.append(list(map(int, input().split())))
print(lst)
'''

'''
4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4
'''
from collections import defaultdict

a, b, c = map(int, input().split())
graph = [[False] * (a + 1) for _ in range(a + 1)]

for _ in range(b):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


visited = [False] * (a + 1)  # dfs의 방문기록

def dfs(V, ret):
    visited[V] = True  # 해당 V값 방문처리
    ret.append(V)
    for i in range(1, a + 1):
        if not visited[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i,ret)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)
ret = []
dfs(c, ret)
print(ret)

'''
lst = []

for _ in range(b) :
    lst.append(list(map(int,input().split())))
print(lst)
#print(sorted(lst))
adj_lst = defaultdict(list)

for u, v in lst :
    adj_lst[u].append(v)
    
print(adj_lst)
def dfs(node, visited, result) :
    visited.add(node)
    result.append(node)
    for i in adj_lst.get(node,[]) :
        if i not in visited :
            dfs(i, visited, result)
result = []
visited = set()
dfs(c, visited, result)


result = ' '.join(map(str, result))
print(result)


'''


