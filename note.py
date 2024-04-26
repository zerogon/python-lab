'''
myString	result
"abcdevwxyz"	"lllllvwxyz"
"jjnnllkkmm"	"llnnllllmm"
'''

n = 3
answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n) :
    answer[i][i] = 1

    
print(answer)