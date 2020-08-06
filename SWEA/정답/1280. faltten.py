for t in range(1, 11):
    dump = int(input())
    dust = list(map(int, input().split()))
    while dump != 0:
        dust.sort(reverse=True)
        dust[0] -= 1
        dust[99] += 1
        dump -= 1
    result = dust[1] - dust[98]
    print(f'#{t} {result}')
        