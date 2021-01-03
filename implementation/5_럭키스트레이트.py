n = list(input())

front_sum = 0	// 앞의 절반의 합
back_sum = 0	// 뒤의 절반의 합

for i in range(len(n)):
	if i < (len(n) // 2):	// 앞의 절반까지
		front_sum += int(n[i])
	else:			// 나머지 뒤의 절반 계산
		back_sum += int(n[i])	

if front_sum == back_sum:
	print("LUCKY")
else:
	print("READY")