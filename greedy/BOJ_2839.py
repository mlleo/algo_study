n = int(input())

result = 0
 
while True:
    if (n % 5) == 0:
        result += n // 5
        break
    else:
        n -= 3
        result += 1
        if n == 0:
            break
       
        if n < 0:
            result = -1
            break
print(result)
