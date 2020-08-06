T = int(input())

for tc in range(1, T + 1):
    ls = list(map(int, input().split()))
    ln = len(ls)
    nl = []
    nnl = []
    for i in range(1<<ln):
        temp = []
        for j in range(ln):
            if i & (1<<j):
                temp += [ls[j]]
        if len(temp) == 3:
            nl += [sum(temp)]
    for i in nl:
        if nnl.count(i) == 0:
            nnl += [i]
    nnl.sort(reverse=True)
    print(f'#{tc} {nnl[4]}')

