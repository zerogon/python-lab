'''
my_string	result
"i love you"	["i", "love", "you"]
"programmers"	["programmers"]
'''
my_string = "i  love you"

answer = [ v for v in my_string.split(" ") if v != '']

