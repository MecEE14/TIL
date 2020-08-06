T = int(input())
for test in range(1, T + 1):
    print(f'#{test}')
    V = int(input())
    ls = []
    for num in range(1, V + 1):
        a, b = map(str, input().split())
        n = int(b)
        for i in range(1, n + 1):
            ls += [a]
    ln = len(ls)
    for i in range(0, ln):
        if (i + 1 == ln):
            print(f'{ls[i]}')
        elif (i + 1) % 10 != 0:
            print(f'{ls[i]}', end='')
        
        else:
            print(f'{ls[i]}')


