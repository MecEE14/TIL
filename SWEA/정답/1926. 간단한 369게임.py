clap = int(input())
for i in range(1, clap + 1):
    nums = list(f'{i}')
    thr = nums.count('3')
    six = nums.count('6')
    nine = nums.count('9')
    res = thr + six + nine
    if res == 0:
        print (f'{i}', end=' ')
    elif res == 1:
        print ('-', end=' ')
    elif res == 2:
        print ('--', end=' ')