import math

T = int(input())

for test in range(1, T + 1):
    n = int(input())
    ls = list(map(int, input().split()))
    result = 0
    z = 0
    for i in ls:
        result += i
    result = result / n
    for j in ls:
        if j <= result:
            z += 1
    print(f'#{test}', end=' ')
    print(f'{z}')
