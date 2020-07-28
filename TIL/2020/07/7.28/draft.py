
T = int(input())

for test in range(1, T + 1):
    ln = int(input())
    nums = list(map(int, input().split()))
    benefit = 0
    while nums != []:
        ls = len(nums)
        bought = 0
        for i in range(0, ls):
            if nums[i] == max(nums):
                if i == 0:
                    nums.remove(nums[0])
                else:
                    for j in range(0, i):
                        bought += nums[j]
                    benefit += ((i * nums[i]) - bought)
                    k = 0
                    while k != i:
                        nums.remove(nums[0])
                        k += 1
                break
    print(f'#{test}', end=' ')
    print(benefit)



