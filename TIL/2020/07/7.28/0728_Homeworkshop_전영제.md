## 0728_Homeworkshop_전영제

### Homework

#### #1

``` python
dic = [8,6,5,7,1,10,68,13,85]
dic2 = [8,6,5,7,1,10,68,13,85]
print(sorted(dic))
dic2.sort()
print(dic2)
------------
sorted()는 원본을 건드리지 않고 정렬된 데이터를 새로 반환해주지만
list_name.sort()는 원본 데이터를 정렬시킨 뒤 반환하는 값은 None이다.
```



#### #2

``` python
ls = [1, 2, 3, 4, 5]
ls2 = [1, 2, 3, 4, 5]
ls.append(7)
ls2.extend('7') # int is not iterable
print(ls2, ls)
------------
extend는 iterable한 데이터만 리스트에 추가할 수 있다.
```



#### #3

``` python
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5

print(a, b)
------------
변수에 원본을 할당 할 경우, 값의 주소가 변수에 입력되기 때문에 2차 변수에 1차 변수를 할당하여도 원본의 주소가 2차 변수에 저장이 된다.
따라서 2차 변수에서 데이터를 건드릴 경우 원본이 수정되는 결과를 낳는다.
이를 방지하려면 
b = a[:] 의 슬라이스를 이용하거나,
import copy
b = copy.deepcopy(a) 를 이용하여 새로운 주소와 원본을 할당해야 한다.
```



### Workshop

#### #1

``` python
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
```



#### #2

``` python
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
```



#### #3

``` python
def lonely(nums):
    result = []
    ln = len(nums)
    for i in range(1, ln):
        if nums[i] != nums[i - 1]:
            result += [nums[i - 1]]
    result += [nums[ln - 1]]
    return result

print(lonely([4, 4, 4, 3, 3]))
```

