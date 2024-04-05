'''
myString	pat	result
"ABBAA"	"AABB"	1
"ABAB"	"ABAB"	0
'''
myString, pat = "ABBAA"	,"AABB"

myString = myString.replace("A","C").replace("B","A").replace("C","B")
print(int(pat in myString.replace("A","C").replace("B","A").replace("C","B") ))


