test = int(input())
for t in range(1, test + 1):
    K, N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    road = []
    for i in range(0, N + 1):
        road += [0]
    for j in ls:
        road[j] = 1
    def counting(road):
        s = 0
        count = 0
        k = K
        while s < N - K:
            if k == 0:
                return 0
            elif road[s + k] == 1:
                 count += 1
                 s += k
                 k = K
            else:
                k -= 1
        return count
    result = counting(road)

    print(f'#{t} {result}')

