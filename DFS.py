'''

graph
[['A','B'],['B','C'],['C','D'],['D','E']
[['A','B'],['A','C'],['B','D'],['B','E'],['C','F'],['E','F']]

start
'A'

1. 노드가 없을 때까지 탐색
2. 가장 최근 노드 인지
3. 이미 방문여부 
'''

from collections import defaultdict
gragh = [['A','B'],['A','C'],['B','D'],['B','E'],['C','F'],['E','F']]
start = 'A'
def solution(gragh, start) :
    adj_list = defaultdict(list)
    for u, v in gragh :
        adj_list[u].append(v)

    def dfs(node, visited, result) :
        visited.add(node)
        result.append(node)
        for neighbor in adj_list.get(node,[]) :
            if neighbor not in visited :
                dfs(neighbor, visited, result)
    visited = set()
    result = []
    dfs(start, visited, result)
    return result
lst = solution(gragh, start)
print(lst)


#43162
n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def dfs(computers , visited, node ):
    visited[node] = True
    for i, connected  in enumerate(computers[node]) :
        if connected and not visited[i] :
            dfs(computers, visited, i)
    
def solution(n, computers) :
    answer = 0 
    visited = [False] * n
    for i in range(n) :
        if not visited[i] :
            dfs(computers, visited, i)
            answer += 1
    return answer 


print(solution(n,computers))