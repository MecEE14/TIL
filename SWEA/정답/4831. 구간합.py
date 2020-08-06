T = int(input())

for test in range(1, T + 1):
    n , m = map(int, input().split())
    nums = list(map(int, input().split()))
    min_sum = 0
    max_sum = 0
    result = 0
    for k in range(0, n):
        min_sum += nums[k]
    for i in range(0, n - m + 1):
        tem_sum1 = 0
        tem_sum2 = 0
        for j in range(0, m):
            tem_sum1 += nums[i + j]
            tem_sum2 += nums[i + j]
        if min_sum > tem_sum1:
            min_sum = tem_sum1
        if max_sum < tem_sum2:
            max_sum = tem_sum2
    result = max_sum - min_sum
    print(f'#{test} {result}')
