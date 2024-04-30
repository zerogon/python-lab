'''
s	result
"[](){}"	3
"}]()[{"	2
"[)(]"	0
"}}}"	0


0	"[](){}"	O
1	"](){}["	X

2	"(){}[]"	O  ['[']

3	"){}[]("	X
4	"{}[]()"	O
5	"}[](){"	X
'''

s = "[)(]"
answer = 0
stack = []
for i in range(len(s)):
    # 올바른 문자열 확인
    for j in s :
        if j == "[" :
            stack.append(j)
        elif j == "(" :
            stack.append(j)
        elif j == "{" :
            stack.append(j)
        elif j == "]" :
            if stack :
              stack.pop()
        elif j == ")" :
            if stack :
               stack.pop()
        elif j == "}" :
            if stack :
              stack.pop()
    # 맨 앞글자를 맨 뒤로 이동
    print(i, stack)
    if len(stack) == 0 :
      answer +=1
      

    lst = list(s)
    lst.append(lst.pop(0))
    s = "".join(lst)
    stack.clear()
print(answer)