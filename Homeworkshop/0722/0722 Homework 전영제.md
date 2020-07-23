## 0722 Homework 전영제

### 1

```python
print()
list()
len()
sum()
str()
int()
```



### 2

```python
def get_middle_char(name):
    a = list(name)
    b = int(len(a) / 2)
    if len(a) % 2 == 0:
        print(a[b - 1] + a[b])
    else:
        print(a[b])
get_middle_char('가나다라마바사')
```



### 3

```python
def ssafy(name, location = '서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy('허준')
ssafy(location = '대전', name = '철수')
ssafy('영희', location = '광주')
#ssafy(name = '길동', '구미')------오류
```



### 4

``` python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
print(result) # -> None
None 이 저장됨
```



### 5

``` python
def my_avg(*nums):
    mysum = 0
    l = len(nums)
    for i in range(0, l):
        mysum += nums[i]
    print(mysum / l)
my_avg(1, 2, 3, 4, 5, 6)
```

