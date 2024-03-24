'''
"rermgorpsam"	[[2, 3], [0, 7], [5, 9], [6, 10]]	"programmers"
'''

my_string, queries = "rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]

list = [i for i in my_string]
#progrmersam
a = list[0:3].reverse()
print(a)


#for a, b in queries :
 #   list[a], list[b] = list[b], list[a]

#answer = "".join(list)
#print(answer)
'''
[2, 3]	"remrgorpsam"
[0, 7]	"progrmersam"
[5, 9]	"prograsremm"
[6, 10]	"programmers"
'''


