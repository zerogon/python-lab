'''
board	k	result
[[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]]	2	8

'''

board = [[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]]
k = 2
answer = 0
for i in range(len(board)) :
    for j in range(len(board[i])) :
        if i + j <= k :
          answer += board[i][j]
print(answer)
