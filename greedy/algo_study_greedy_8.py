n = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort()

result = 1

for coin in coin_list:
	if result < coin:
		break
	result += coin

print(result)
	

		

