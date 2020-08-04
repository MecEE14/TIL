T = int(input())

for i in range(1, T + 1):
    print(f'#{i}')
    num = int(input())
    line = [1, 1]
    for p in range(1, num + 1):
        re_line = []
        if p == 1:
            print(1)
        elif p == 2:
            print('1 1')
        elif p == 3:
            line = [1, 2, 1]
            for i in line:
                print(i, end=' ')
            print('')
        else:
            re_line += [1]
            for j in range(0, p - 2):
                re_line += [line[j] + line[j + 1]]
            re_line += [1]
            line = re_line[:]
            for k in line:
                print(k, end=' ')
            print('')
            