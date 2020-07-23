## 0723 Workshop 전영제

### 1

``` python
$def get_secret_word(num):
$    result = ''
$    for i in num:
$        result += chr(i)
$    print(result)
$	 return result
$get_secret_word([83, 115, 65, 102, 89])

```



### 2

``` python
$def get_secret_number(name):
$    list_name = list(name)
$    result = 0
$    for i in list_name:
$        result += ord(i)
$    print(result)
$	 return result
$get_secret_number('john')

```



### 3

``` python
$def get_strong_word(a, b):
$    lista = list(a)
$    listb = list(b)
$    resulta = 0
$    resultb = 0
$    for i in lista:
$        resulta += ord(i)
$    for j in listb:
$        resultb += ord(j)
$    if resulta > resultb:
$        print(a)
$		 return a
$    elif resultb> resulta:
$        print(b)
$		 return b
$    else:
$        print('두 이름의 아스키코드 숫자 합이 같습니다.')
$get_strong_word('john', 'nojh')

```

