'''
num_list	result
[4, 2, 6, 1, 7, 6]	17
[-1, 2, 5, 6, 3]	8
'''
num_list = [4, 2, 6, 1, 7, 6]	
answer = 0
odd = 0
even = 0
for i, v in enumerate(num_list) :
     if i % 2 : 
          odd += v
     else :
          even += v
answer = max(odd,even)       
sum = 0
