T = int(input())

for tc in range(1, T + 1):
    N, maxcal = map(int, input().split())
    ls = []
    mls = []
    for i in range(1, N + 1):
        ls += [list(map(int, input().split()))]
    for i in range(1<<N):
        score = 0
        cal = 0
        for j in range(N):
            if i & 1<<j:
                cal += ls[j][1]
                score += ls[j][0]
        if cal <= maxcal:
            mls += [score]
    print(f'#{tc} {max(mls)}')