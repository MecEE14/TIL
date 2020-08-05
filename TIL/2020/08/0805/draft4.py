for t in range(1, 11):
    tc = int(input())
    ls = []
    sum_ls = []
    for i in range(100):
        ls += [list(map(int, input().split()))]
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += ls[i][j]
        sum_ls += [temp]
    for j in range(100):
        temp = 0
        for i in range(100):
            temp += ls[i][j]
        sum_ls += [temp]
    temp = 0
    for k in range(100):
        temp += ls[k][k]
    sum_ls += [temp]
    temp = 0
    for K in range(100):
        temp += ls[K][99 - K]
    sum_ls += [temp]
    sum_ls.sort()
    print(f'#{tc} {sum_ls[-1]}')
    
