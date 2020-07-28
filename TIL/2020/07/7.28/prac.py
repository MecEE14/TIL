'''
def is_pal_while(word):
    
    rev = ''
    ls = list(word)
    ln = len(word)
    i = ln
    while i != 0:
        rev += ls[i - 1]
        i -= 1
    if rev == word:
        return True
    else:
        return False

print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))
'''
'''
def is_pal_while(word):
    word2 = word
    def fx(word2):
        ls = list(word2)
        ln = len(word2)
        if ln > 0:
            a = ls.pop(ln - 1)
            word2 = ls
            return a + fx(word2)
        else:
            return ''
    result = fx(word)
    if result == word:
        return True
    else:
        return False
print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))
'''
'''
#교수님 풀이
def is_pal(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_pal(word[1:-1])
    else:
        return False

print(is_pal('tomato'))
print(is_pal('racecar'))
print(is_pal('azza'))
'''
'''
def is_pal(word):
    return word[::-1] == word
'''
# prac 2
# 중복되지 않은 숫자의 합
'''
def sum_of_repeat_number(numbers):
    result = 1
    for i in numbers:
        if numbers.count(i) == 1:
            result *= i
    return result

print(sum_of_repeat_number([4, 4, 7, 8, 10]))
'''
'''
# 썩은 과일 찾기
def change_rotten_fruit(fruit_bag):
    bag = []
    for i in fruit_bag:
        ls = list(i)
        ln = len(ls)
        result = ''
        name = ''
        if ln > 6:
            for j in range(0, 6):
                result += ls[j]
            if result == 'rotten':
                for j in range(6, ln):
                    if ord(ls[j]) < 97:
                        ls[j] = chr(ord(ls[j]) + 32)
                        name += ls[j]
                    else:
                        name += ls[j]
            bag += [name]
        else:
            bag += [i]
    return bag

print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))
'''