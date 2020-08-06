T = int(input())

for test_case in range(1, T + 1):
    m, n = map(int, input().split( ))
    cube = []
    max_result = 0
    for i in range(0, m):
        cube += [list(map(int, input().split( )))]
    for i in range(0, m - n + 1):
        result = 0
        for j in range(0, m - n + 1):
            for k in range(0, n):
                for z in range(0, n):
                    result += cube[j + k][i + z]
            if result >= max_result:
                max_result = result
                result = 0
            else:
                result = 0
    print(f'#{test_case}', end=' ')
    print(max_result)


