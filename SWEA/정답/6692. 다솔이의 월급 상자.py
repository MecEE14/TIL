T = int(input())

for t in range(1, T + 1):
    tc = int(input())
    ls = []
    for k in range(1, tc + 1):
        a, b = map(float, input().split())
        ls += [a * b]
    result = sum(ls)
    print(f'#{t} {result}')