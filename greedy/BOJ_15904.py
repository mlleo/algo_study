s = list(input())

opt = 0

for i in range(len(s)):
	if opt == 0 and s[i] == 'U':
		opt = 1
	if opt == 1 and s[i] == 'C':
		opt = 2
	if opt == 2 and s[i] == 'P':
		opt = 3
	if opt == 3 and s[i] == 'C':
		opt = 4
if opt == 4:
	print("I love UCPC")
else:
	print("I hate UCPC")

