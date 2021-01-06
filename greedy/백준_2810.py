n = int(input())
data = input()

couple = data.count('LL')

if couple <= 1:
    print(n)
else:
    print(n+1-couple)