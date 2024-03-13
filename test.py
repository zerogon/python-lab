a = "He11oWor1d"
b = "lloWorl"
# aBcDeFg
# AbCdEfG
answer = ""
'''
for i in range(len(a)) :
    if a[i] == a[i].lower() :
        answer += a[i].upper()
    else :
        answer += a[i].lower()
'''
#print(answer)

#print('''!@#$%^&*(\\'"<>?:;''')

#a, b = map(int, input().strip().split(' '))
#print(a, '+', b,'=',a+b)

# 대소문자 변경
#print(a.swapcase())

'''
"He11oWor1d"	"lloWorl"	2	"HelloWorld"
"Program29b8UYP"	"merS123"	7	"ProgrammerS123"
'''
c = 2
print(a[0:c] + b + a[len(b)+len(a[0:c]):])


