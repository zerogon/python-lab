
'''
네개가 같은 "rermgorpsam"	[[2, 3], [0, 7], [5, 9], [6, 10]]	"programmers"
'''
my_string, queries = "rermgorpsam",	[[2, 3], [0, 7], [5, 9], [6, 10]]

answer = ''
for a, b in queries :
   my_string = my_string[0:a]+"".join(my_string[a:b+1][::-1])+my_string[b+1:]

print(my_string[0:3][::-1])

