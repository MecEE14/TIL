T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = [1, 2, 3, 4, 5, 6 ,7, 8, 9 ,10, 11, 12]
    count = 0
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1<<j):
                temp += [nums[j]]
        if len(temp) == N:
            if sum(temp) == K:
                count += 1
    print(f'#{tc} {count}')
