
box = []
box += [list(map(int, input().split())) for i in range(19)]

def row(ls_box, color):
    col = [4, 9, 14]
    for i in range(19):
        for j in col:
            cnt = 0
            for k in range(-4, 5):
                if ls_box[i][j + k] == color:
                    cnt += 1
            if cnt == 5:
                return (i + 1, j- 3)
    return False

def column(ls_box, color):
    col = [4, 9, 14]
    for i in range(19):
        for j in col:
            cnt = 0
            for k in range(-4, 5):
                if ls_box[j + k][i] == color:
                    cnt += 1
            if cnt == 5:
                return (i + 1, j- 3)
    return False

def diag(ls_box, color):
    for i in range(15):
        for j in range(15):
            cnt = 0
            x = 0
            while (i + x) <18 and (j + x) < 18:
                if ls_box[i + x][j + x] == color:
                    cnt += 1
                    if cnt == 5:
                        if ls_box[i + x + 1][j + x + 1] != color:
                            return (i + x - 3, j + x - 3)
                        else:
                            cnt = 0
                    x += 1
                elif ls_box[i + x][j + x] != color:
                    cnt = 0
                    x += 1
                else:
                    x += 1
    return False

def r_diag(ls_box, color):
    for i in range(15):
        for j in range(18, 3, -1):
            cnt = 0
            x = 0
            while (i + x) <19 and (j - x) < 19:
                if ls_box[i + x][j - x] == color:
                    cnt += 1
                    if cnt == 5:
                        if ls_box[i + x + 1][j - x - 1] != color:
                            return (i + x - 3, j - x + 3)
                        else:
                            cnt = 0
                    x += 1
                elif ls_box[i + x][j - x] != color:
                    cnt = 0
                    x += 1
                else:
                    x += 1
    return False


print(row(box, 1))
print(column(box, 1))
print(diag(box, 1))
print(r_diag(box, 1))

'''
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
0 0 2 0 0 2 2 2 1 0 0 0 0 0 0 0 1 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 1 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''