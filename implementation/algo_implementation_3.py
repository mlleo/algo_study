data = input()

column = int(data[0]) - int(ord('a')) + 1
row = data[1] 

count = 0

d_col = [2, 2, -2, -2, 1, 1, -1, -1]
d_row = [-1, 1, -1, 1, 2, -2, 2, -2]

for i in range(8):
	new_col = column + d_col[i]
	new_row = row + d_row[i]
	
	if 1<= new_col and new_col <=8 and 1<= new_row and new_row <= 8:
		count += 1

print(count)