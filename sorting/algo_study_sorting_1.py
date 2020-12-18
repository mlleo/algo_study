n = int(input())

data = []

for _ in range(n):
	data.append(int(input()))

data.sort(reverse = True)

for i in data:
	print(data[i], end=' ')
