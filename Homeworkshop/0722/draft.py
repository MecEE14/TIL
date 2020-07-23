# 2 번 문제
'''
def get_middle_char(name):
    a = list(name)
    b = int(len(a) / 2)
    if len(a) % 2 == 0:
        print(a[b - 1] + a[b])
    else:
        print(a[b])
get_middle_char('가나다라마바사')
'''

# 3 번 문제
'''
def ssafy(name, location = '서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy('허준')
ssafy(location = '대전', name = '철수')
ssafy('영희', location = '광주')
#ssafy(name = '길동', '구미')      오류
'''

# 4 번 문제
'''
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
print(result) # -> None
'''

# 5 번 문제
'''
def my_avg(*nums):
    mysum = 0
    l = len(nums)
    for i in range(0, l):
        mysum += nums[i]
    print(mysum / l)
my_avg(1, 2, 3, 4, 5, 6)
'''

# Workshop
# 1 번 문제
'''
def list_sum(*nums):
    result = 0
    for i in nums:
        if type(i) == int:
            result += i
        else:
            result = '정수를 입력하세요'
            break
    print(result)
list_sum(1, 2, 3, 4, 5, 6)
'''
'''
#2 번 문제
def dict_list_sum(*kw):
    result = 0
    l = len(kw)          #Dic 의 갯수 ex) 2
    for i in range(0, l):
        b = kw[i]        #튜플
        #print(b)
        c = len(b)
        for j in range(0, c):     #Dic[0], dic[1]
            d = list(b[j].values())
            print(d)
            for k in d:
                if type(k) == int:
                    result += k
    print(result)
            
            
    


dict_list_sum([{'영제': 1, '상재': 3}, {'킹제': '1', '킹제1': 4, '킹제2': 5}], [{'흑제': 1, '둔재': 2}])
'''

# 3 번 문제
def all_list_sum(*ls):
    result = 0
    for i in ls:
        for j in i:
            result += j
    print(result)
            






all_list_sum([1], [2, 3], [4, 5, 6], [7, 8, 9, 10])