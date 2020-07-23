## 0722 Workshop 전영제

### 1

``` python
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
```



### 2

``` python
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
```



### 3

```python
def all_list_sum(*ls):
    result = 0
    for i in ls:
        for j in i:
            result += j
    print(result)
```

