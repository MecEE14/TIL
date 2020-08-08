T = int(input())

for tc in range(1, T + 1):
    box = []
    box += [list(map(int, input().split())) for i in range(9)]
    proof = 0
    nums = [1, 4, 7]
    deltax = [0, 0, 0, 1, -1, 1, -1, -1, 1]
    deltay = [0, 1, -1, 0, 0, 1, -1, 1, -1]
    for i in range(9):
        temp = 0
        if sum(box[i]) != 45:
            proof += 1
        for j in range(9):
            temp += box[j][i]
        if temp != 45:
            proof += 1
    for i in nums:
        temp = 0
        for j in range(9):
            temp += box[i + deltax[j]][i + deltay[j]]
        if temp != 45:
            proof += 1
    if proof == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

    

            