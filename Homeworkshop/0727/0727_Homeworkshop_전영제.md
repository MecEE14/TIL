## 0727_Homeworkshop_전영제

### Homework

#### 1 

``` python
def count_vowels(word):
    a = word.count('a')
    e = word.count('e')
    i = word.count('i')
    o = word.count('o')
    u = word.count('u')
    nums = a + e + i + o + u
    return nums
print(count_vowels('banana'))
```



#### 2

``` python
4번
```



#### 3

``` python
def only_square_area(a, b):
    area = []
    for i in a:
        for j in b:
            if i == j:
                area += [i ** 2]
    return area

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
```



### Workshop

#### 1

``` python
def get_dict_avg(nums):
    nums_list = list(nums.values())
    result = 0
    for i in nums_list:
        result += i
    result = result/len(nums_list)
    return result

print(get_dict_avg({
    'python': 80,
    'algorithm': 90,
    'django': 89,
    'web': 83
}))
```



#### 2

``` python
def count_blood(bloods):
    A = bloods.count('A')
    AB = bloods.count('AB')
    B = bloods.count('B')
    O = bloods.count('O')
    result = {
        'A': A,
        'B': B,
        'AB': AB,
        'O': O
    }
    return result
```

