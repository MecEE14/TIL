def row_sum(a):
    for i in range(0,9):
        if sum(a[i]) != 45:
            return False
    return True

def col_sum(a):
    for i in range(0, 9):
        col = 0
        for j in range(0, 9):
            col += a[j][i]
        if col != 45:
            return False
    return True

def box_sum(a):
    ls = [0, 3, 6]
    lk = [0, 1 ,2]
    for i in ls: # 0 3 6
        box = 0
        for j in lk: # 0 1 2
            for k in lk: # 0 1 2
                box += a[i + k][j]
        if box != 45:
            return False
    return True
        

T = int(input())

for test in range(1, T + 1):
    sdo = []
    result = 0
    ran = range(0, 9)
    for i in range(1, 10):
        row = list(map(int, input().split()))
        sdo += [row]
    b1 = row_sum(sdo)
    b2 = col_sum(sdo)
    b3 = box_sum(sdo)
    if b1 and b2 and b3:
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')






#for test in range(1, T + 1):