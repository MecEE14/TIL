T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    box = [list(map(int, input().split())) for i in range(N)]
    a, b = 1, 1
    result = []
    def find(n, tbox):
        a, b = 0, 0
        sa, sb = 0, 0
        for i in range(n):
            for j in range(n):
                if box[i][j] != 0:
                    sa, sb = i, j
                    while (i + a) < n and box[i + a][j] != 0:
                        a += 1
                    while (j + b) < n and box[i][j + b] != 0:
                        b += 1
                    return a, b, sa, sb
        return False
            
    def erase(n, box, sa, sb):
        for i in range(sa, sa +a):
            for j in range(sb, sb +b):
                box[i][j] = 0 
    cnt = 0
    while find(N, box):
        cnt += 1
        a, b, sa, sb = find(N, box)
        erase(N, box, sa, sb)
        result += [[a, b]]
    
    for i in range(0, len(result)):
        for j in range(0, len(result) - 1):
            if result[j][0] * result[j][1] > result[j + 1][0] * result[j + 1][1]:
                result[j], result[j + 1] = result[j + 1], result[j]
            elif result[j][0] * result[j][1] == result[j + 1][0] * result[j + 1][1]:
                if result[j][0] > result[j + 1][0]:
                    result[j], result[j + 1] = result[j + 1], result[j]




    print(f'#{tc} {cnt}', end=' ')
    for i in result:
        print(f'{i[0]} {i[1]}', end=' ')
    print('')
    




