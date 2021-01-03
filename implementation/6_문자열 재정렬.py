s = list(input())

num = 0		// 숫자 합을 계산
arr = []

for i in len(s):
	if s[i].isdigit():	// 숫자인 경우
		num += int(s[i])
	else:		// 문자인 경우
		arr.append(s[i])

arr.sort()
arr.append(num)

for i in arr:
	print(i, end='')


