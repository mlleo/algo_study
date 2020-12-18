n = int(input())

data = []

for _ in range(n):
	a,b = input().split()
	data.append((a,b))

result = sorted(data, key = lambda x: int(x[1]))

for i in result:
	print(i[0], end = ' ')