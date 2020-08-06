T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    ls = []
    for m in range(M):
        ls += [list(map(int, input().split()))]
    count = 0
    ln = len(ls)
    nls = []
    for i in range(1<<ln):
        temp = []
        for j in range(ln):
            if i & (1<<j):
                temp += [ls[j]]
        if len(temp) == 3:
            nls += [temp]
    print(nls)