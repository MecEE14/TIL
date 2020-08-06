T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0 for i in range(1, N + 1)]
    for q in range(1, Q + 1):
        L, R = map(int, input().split())
        for n in range(L - 1, R):
            box[n] = q
    print(f'#{tc}', end=' ')
    for i in range(0, N):
        print(f'{box[i]}', end=' ')
    print('')