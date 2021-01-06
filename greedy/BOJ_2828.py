n,m = map(int, input().split())
j = int(input())

front = 1
back = m

result = 0

for _ in range(j):
	data = int(input())
	if data < front:
		move = front-data
		front -= move
		back -= move
		result += move
	elif front <= data and data <= back:
		continue
	else:
		move = data-back
		front += move
		back += move
		result += move

print(result)
