T = int(input())

for tc in range(1, T + 1):
    D, A, B ,F = map(int, input().split())
    H = D / (abs(A + B))
    L = H * F
    print(f'#{tc} {L}')
