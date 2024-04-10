'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''

from collections import defaultdict

gragh = [[1,2], [1,3], [1,4], [2,4],[3,4]]
def solution(start, gragh) :
    adj_list = defaultdict(list)
    for u, v in gragh :
        adj_list[u].append(v)

    def dfs(node, visited, result) :
        visited.add(node)
        result.append(node)
        for i in adj_list.get(node,[]) :
            if i not in visited :
                dfs(i, visited, result)

    visited = set()
    result = []
    dfs(start, visited, result)
    return result
lst = solution(1, gragh)
print(lst)