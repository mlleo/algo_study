n = int(input())

data = list(input().split())

direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1

for i in data:
	for j in range(len(direction)):
		if i == direction[j]:
			new_x = x + dx[j]
			new_y = y + dy[j]
	if new_x  < 1 or new_y < 1 or new_x > n or new_y > n:
		continue		
	x = new_x
	y = new_y
	
print(x, y)