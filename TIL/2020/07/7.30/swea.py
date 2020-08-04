T = int(input())
for test in range(1, T + 1):
    N = int(input())
    init = 1
    ls = []
    for i in range(0, N):
        in_lis = []
        for j in range(0, N):
            in_lis += [j]
        ls += [in_lis]
    #print(ls)
    def odd_box(num):
        global N
        global init
        if num == 1:
            ls[N - 1 - N//2][N - 1 - N//2] = init
            return ls
        else:
            for a in range(0, num):
                ls[0][a] = init
                init += 1
                #print(ls)
            for b in range(1 , num):
                ls[b][num - 1] = init
                init += 1
                #print(ls)
            for c in range(num - 2, -1, -1):
                ls[num - 1][c] = init
                #print(ls)
                init += 1
            for d in range(num - 2, 0, -1):
                ls[d][0] = init 
                init += 1
                #print(ls)
        return odd_box(num - 2)
    def even_box(num):
        global init
        for a in range(0, num):
            ls[0][a] = init
            init += 1
        for b in range(0 , num):
            ls[b][num - 1] = init
            init += 1
        for c in range(num - 1, 0):
            ls[num][c] = init
            init += 1
        for d in range(num - 1, 0):
            ls[d][0] = init 
            init += 1
        num -= init
        return even_box(num)
    if N % 2 == 0:
        print(even_box(N))
    else:
        print(odd_box(N))

        
        
