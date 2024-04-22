'''
d	budget	result
[1,3,2,5,4]	9	3
[2,2,3,3]	10	4


1 2 3 4 5

9 - 1 = 8 answer + 1  > 2
8 - 2 = 6 answer + 1  > 2
6 - 3 = 3 answer + 1  < 4

'''
d, budget = [2,2,3,3], 10
answer = 1

# 정렬한다
# 앞에서부터 값을 budget값에서 뺀다 뺀값이 다음값보다 크면 빼고 answer값 증가한다.
# 뺀 값이 다음값보다 작으면 멈춘다

d.sort()
for i,v in enumerate(d) :
    if (budget - v) > d[i+1] :
        budget -= v 
        answer += 1
    else :
        break

print(answer)




    

