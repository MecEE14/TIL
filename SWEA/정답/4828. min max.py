test = int(input())                             #  테스트 케이스를 입력
'''
# min, max를 사용함
for i in range(1, test + 1):                    # 각각의 테스트 케이스에서

    num = int(input())                          # 입력 될 총 숫자의 갯수
    nums = list(map(int, input().split()))      # 리스트 형태로 숫자들을 입력
    max_num = max(nums)                         # 가장 큰 수
    min_num = min(nums)                         # 가장 작은 수
    result = max_num - min_num                  # 차이값
    print(f'#{i} {result}')                     # 출력
    '''
for j in range(1, test + 1):

    num = int(input())
    nums = list(map(int, input().split()))
    nums.sort()                                 # 리스트를 .sort() 메서드로 정렬
    result = abs(nums[0] - nums[num - 1])       # 끝 단의 두 값의 차의 절대값을 반환
    print(f'#{j} {result}')                     # 출력