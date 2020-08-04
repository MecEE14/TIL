T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ls = list(map(int, input()))
    counting = 0
    count_num = 0
    for i in range(0, 10):
        if ls.count(i) > counting:
            counting = ls.count(i)
            count_num = i
        elif ls.count(i) == counting:
            if count_num < i:
                count_num = i
    print(f'#{t} {count_num} {counting}')