T = int(input())
for tc in range(1, T + 1):
    box = [[0 for i in range(10)] for i in range(10)]
    N = int(input())
    count = 0
    for i in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for R in range(r1, r2 + 1):
            for C in range(c1, c2 + 1):
                box[R][C] += c
                if box[R][C] == 3:
                    count += 1
    print(f'#{tc} {count}')
