'''
arr	n	result
[49, 12, 100, 276, 33]	27	[76, 12, 127, 276, 60]
[444, 555, 666, 777]	100	[444, 655, 666, 877]
'''
arr	, n = [49, 12, 100, 276, 33],	27
gksghk455
# arr 의 길이가 홀수 인 경우 -> 짝수 인덱스에 n값 더하기 
# arr 의 길이가 짝수 인 경우
if len(arr) % 2 : 
    for i, v in enumerate(arr) :
        if not i % 2 :
            arr[i] = arr[i] + n
else :
    for i, v in enumerate(arr) :
        if i % 2 :
            arr[i] = arr[i] + n
print(arr)
