n = int(input())
data= map(int, input().split())
'''
딸기 우유 : 0, 초코 우유: 1, 바나나 우유: 2
규칙에 따르면 0, 1, 2, 0, 1, 2, ... 순으로 우유를 마셔야 함
'''

first = 0		// 맨 처음에는 딸기우유
count = 0		// 우유 갯수

for milk in data:
	if milk == (first % 3):	// first 값을 순차적으로 증가시키면서 3으로 나눈 나머지를 통해 비교
		count += 1
		first += 1
print(count)
