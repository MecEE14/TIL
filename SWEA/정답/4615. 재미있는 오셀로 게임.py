T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    bod = [[0 for i in range(N)] for j in range(N)]
    cen = int(N/2)
    bod[cen][cen] = 2
    bod[cen - 1][cen - 1] = 2
    bod[cen - 1][cen] = 1
    bod[cen][cen - 1] = 1
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    for m in range(M):
        i, j, c = map(int, input().split())
        bod[i - 1][j - 1] = c
        for I in range(0, 8):
            if -1 < (i - 1 + dy[I]) < N and -1 < (j - 1 + dx[I]) < N and bod[i - 1 + dy[I]][j - 1 + dx[I]] != c and bod[i - 1 + dy[I]][j - 1 + dx[I]] != 0:
                for z in range(2, N):
                    if -1 < (i - 1 + z * dy[I]) < N and -1 < (j - 1 + z * dx[I]) < N and bod[i - 1 + z * dy[I]][j - 1 + z * dx[I]] == 0:
                        break
                    if -1 < (i - 1 + z * dy[I]) < N and -1 < (j - 1 + z * dx[I]) < N and bod[i - 1 + z * dy[I]][j - 1 + z * dx[I]] != c:
                        continue
                    if -1 < (i - 1 + z * dy[I]) < N and -1 < (j - 1 + z * dx[I]) < N and bod[i - 1 + z * dy[I]][j - 1 + z * dx[I]] == c:
                        for k in range(1, z):
                            bod[i - 1 + k * dy[I]][j - 1 + k * dx[I]] = c
                        break
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if bod[i][j] == 1:
                black += 1
            elif bod[i][j] == 2:
                white += 1
            else:
                continue
    print(f'#{tc} {black} {white}')
    







    