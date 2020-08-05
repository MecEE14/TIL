T = int(input())

for t in range(1, T + 1):
    init = 0
    N = int(input())
    box = [[0 for j in range(N)] for k in range(N)]
    ln = len(box)
    x = 1
    X = -1
    y = 1
    Y = -1
    i = 0
    j = -1
    while N != 0:
        if N != 1:
            j += 1
            init += 1
            box[i][j] = init
            for n in range(0, N - 1):
                init += 1
                j += x
                box[i][j] = init
            for n in range(0, N - 1):
                init += 1
                i += y
                box[i][j] = init
            for n in range(0, N - 1):
                init += 1
                j += X
                box[i][j] = init
            for n in range(0, N - 2):
                init += 1
                i += Y
                box[i][j] = init
            N -= 2
        else:
            if len(box) == 1:
                box[0][0] = 1
                N -= 1
            else:
                box[ln // 2][ln // 2] = init + 1
                N -= 1
    print(f'#{ln}')
    for i in range(ln):
        for j in range(ln):
            print(f'{box[i][j]}', end=' ')
        print('')
