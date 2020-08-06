T = int(input())

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num

def prime_ls(num):
    ls = []
    for i in range(2, num):
        if prime(i):
            ls += [i]
    return ls

def three(ls):                      # 부분 집합 중 원소 3개인 것
    ln = len(ls)
    nnls = []
    for i in range(1<<ln):
        nls = []
        for j in range(ln):
            if i & (1<<j):
                nls += [ls[j]]
        if len(nls) == 3:
            nnls += [nls]
    return nnls



for tc in range(1, T + 1):
    N = int(input())
    ls = prime_ls(N)
    ln = len(ls)
    cnt = 0
    for i in range(ln):
        for j in range(i, ln):
            for k in range(j, ln):
                if (ls[i] + ls[j] + ls[k]) == N:
                    cnt += 1
    print(f'#{tc} {cnt}')

    

        
    

