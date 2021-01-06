n = int(input())
change = 1000-n
count = 0
coin_list = [500,100,50,10,5,1]

for coin in coin_list:
	count +=  change // coin
	change %= coin

print(count)
