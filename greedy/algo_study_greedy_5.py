n = int(input())
data = list(map(int, input().split()))

data.sort()

group = 0
member = 0

for score in data:
	member += 1
	if score <= member:
		group += 1
		member = 0

print(group)
	