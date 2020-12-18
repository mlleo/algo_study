n,k = map(int, input().split())
data_A = list(map(int, input().split()))
data_B = list(map(int, input().split()))



for _ in range(k):
	min_A = data_A.index(min(data_A))
	max_B = data_B.index(max(data_B))
	data_A[min_A], data_B[max_B] = data_B[max_B], data_A[min_A]

print(sum(data_A))
	