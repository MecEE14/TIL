T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    temp = []
    for i in range(0, N):
        if i % 2 == 0:
            temp += [nums[N - 1 - int(i/2)]]
        else: 
            temp += [nums[i//2]]
    print(f'#{tc}', end=' ')
    for i in range(0, 10):
        print(temp[i], end=' ')
    print('')








    