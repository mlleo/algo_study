n,m,k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse = True)

first = num[0]
second = num[1]

second_num = m // (k+1)
first_num = m - second_num

result = first * first_num + second * second_num

print(result)