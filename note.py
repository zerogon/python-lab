'''
N = 5
K = 2
answer 3
'''
from collections import deque

N, K = 5, 2
answer = 0

'''
1 2 3 4 5

1 (2) 3 4 5

1 (2) 3 [4] 5

[1] (2) 3 (4) 5

(1) (2) 3 (4) [5]

'''
from collections import deque

queue = deque(range(1))