price = int(input())

coin_list = [500, 100, 50, 10, 5, 1]

money = 1000 - price
count = 0

for coin in coin_list:
	count += (money // coin)
	money %= coin

print(count)