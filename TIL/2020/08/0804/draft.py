T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    numbers = []
    str_nums = []
    max_num = 0
    for a in range(0, N - 1):
        for b in range(a + 1 , N):
            numb = nums[a] * nums[b]
            ls = [str(numb)]
            print(ls)




