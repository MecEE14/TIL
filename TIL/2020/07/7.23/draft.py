# my_abs
'''
def my_abs(num):
    result = 0
    if type(num) == float:
        result = ((num) ** 2) ** 0.5
    else:
        a = num.real
        b = num.imag
        result = ((a ** 2) + (b ** 2)) ** 0.5
    return result
    
print(my_abs(3 + 4j))
'''

# my_all()
'''
def my_all(elements):
    if bool(elements) == False:
        return True
    else:
        for i in elements:
            print(i)
            if bool(i) == False:
                return False
                break
        return True

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([3, 5, [], 2, 5, '6']))
'''

# my_any()
'''
def my_any(elements):
    if bool(elements) == False:
        return False
    else:
        for i in elements:
            print(i)
            if bool(i) == True:
                return True
                break
        return False

print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
'''

# 불쌍한 달팽이 snail()
'''
def snail(a, b, c):
    one = b - c
    i = 1
    while(a - (i * (one)) > 5):
        print(i)
        i += 1
    return i + 1 
print(snail(100, 5, 2))
'''

# 자릿수 더하기 sum_of_digit
'''
def sum_of_digit(num):
    ls = list(str(num))
    result = 0
    for i in ls:
        result += int(i)
    return result

print(sum_of_digit(1234))
print(sum_of_digit(4321))
'''
'''
def get_middle_char(name):
    a = list(name)
    b = int(len(a) / 2)
    if len(a) % 2 == 0:
        result = a[b - 1] + a[b]
        return result
    else:
        result = a[b]
        return result
print(get_middle_char('가나다라라마바사'))
'''

T = int(input())
for n in range(1, T + 1):
    num = list(map(int, input().split()))
    sor = sorted(num)
    ln = len(num)
    result = 0
    for i in range(1, ln - 1):
        result += sor[i]
        avg = int(result / (ln - 2))
    print(f'#{n} {avg}')
