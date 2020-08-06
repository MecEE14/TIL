T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sub = list(map(int, input().split()))
    stu = [i for i in range(1, N + 1)]
    for j in range(0, K):
        stu.remove(sub[j])
        stu.sort
    print(f'#{tc}', end=' ')
    for i in range(0, N - K):
        print(stu[i], end=' ')
    print('')








    