
'''
q	r	code	result
3	1	"q[j]nw[e]zg[r]pi[r]ld[y]wt"	"jerry"


        code	q	j	n	w	e	z	g	r	p	i	r	l	d	y	w	t
       index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15
q로 나눈 나머지	 0 	1	2	0	1	2	0	1	2
'''
# 1 , 5, 9 , 13
q, r, code= 3,	1,	"qjnwezgrpirldywt"

print(code[r::q])






