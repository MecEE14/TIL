T = int(input())
for t in range(1, T + 1):
    a, b = 0, 0
    p, q, r, s, w = map(int, input().split())
    a = p * w
    if w <= r:
        b = q
    else:
        b = q + (s * (w - r))
    if a > b:
        print(f'#{t} {b}')
    else:
        print(f'#{t} {a}')
        
            