'''
my_string	is_suffix	result
"banana"	"ana"	1
"banana"	"nan"	0
"banana"	"wxyz"	0
"banana"	"abanana"	0
'''

my_string, is_suffix = "banana", "nan"
list =  [ my_string[i:] for i in range(len(my_string)) if my_string[i:] == is_suffix]



answer = 1 if len([m[i:] for i in range(len(m)) if m[i:] == s])>0  else 0
'''
 if m[-len(s):]==s: return 1
    return 0
    '''
