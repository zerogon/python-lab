'''
N = 5
result = [[1,2,3,4], [1,4,5], [2,3,5]]
'''

def sol(N) :
    result = []
    def backtrack(sum, selected_nums, start):
        if sum == 10 :
          result.append(selected_nums)
          return
        for i in range(start, N+1) :
          if sum + i <= 10:
              backtrack(
                  sum+i, selected_nums + [i], i+1
              )
    backtrack(0, [], 1)
    return result

print(sol(5)) # 반환값 : [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
