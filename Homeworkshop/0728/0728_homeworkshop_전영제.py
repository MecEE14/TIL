# Homework
# prob 1
'''
dic = [8,6,5,7,1,10,68,13,85]
dic2 = [8,6,5,7,1,10,68,13,85]
print(sorted(dic))
print(dic)
dic2.sort()
print(dic2)
'''

# prob 2
'''
ls = [1, 2, 3, 4, 5]
ls2 = [1, 2, 3, 4, 5]
ls.append([3, 2, 1])
ls2.extend('7') # int is not iterable
print(ls2, ls)
'''

# prob 3
'''
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5

print(a, b)
'''

# Workshop
# prob 1
'''
def duplicated_letters(word):
    ls = list(word)
    result = []
    dic = {}
    for i in ls:
        if ls.count(f'{i}') >=2:
            dic.update({f'{i}': ls.count(i)})
    result += [key for key in dic]
    return result
print(duplicated_letters('banana'))
'''

# prob 2
'''
def low_and_up(word):
    ls = list(word)
    ln = len(word)
    asc = 0
    result = ''
    for i in range(0, ln):
        if i % 2 == 1:
            asc = ord(ls[i]) - 32
            ls[i] = chr(asc)
            result += ls[i]
        else:
            result += ls[i]
    return result
print(low_and_up('banana'))
'''

# prob 3
'''
def lonely(nums):
    result = []
    ln = len(nums)
    for i in range(1, ln):
        if nums[i] != nums[i - 1]:
            result += [nums[i - 1]]
    result += [nums[ln - 1]]
    return result

print(lonely([4, 4, 4, 3, 3]))
'''
