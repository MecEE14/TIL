## 7.20 Homework 전영제

### 1. python 예약어

```python
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

### 2. 실수 비교

```python
import math

num1 = 0.1 * 3
num2 = 0.3

math.isclose(num1, num2)
```

### 3. 이스케이프 시퀀스

|    문제     |  답  |
| :---------: | :--: |
|  1. 줄바꿈  |  \n  |
|    2. 탭    |  \t  |
| 3. 백슬래시 | \\\  |

### 4. String Interpolation

```python
name = '철수'
print(f'안녕, {name}야')
```

### 5. 형 변환

```python
int('3.5')는 오류가 발생한다
int(float('3.5'))로 쓰거나 int(3.5)로 쓴다
```

### 6. 네모 출력

```python
n = 5
m = 9
row = '*'*5
print(f'{row}\n'*m)
```

### 7. 이스케이프 시퀀스 응용

```
print('"파일은 c:\\Window\\Users\\내문서\\Python에 저장이 되었습니다"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지\'')
```

### 8. 근의 공식

```python
A = input('이차항의 계수:')
B = input('일차항의 계수:')
C = input('상수항의 계수:')
a = int(A)
b = int(B)
c = int(C)

if ((b**2)-4*a*c) > 0:
    answer1 = (-b+((b**2)-4*a*c)**0.5)/(2*a)
    answer2 = (-b-((b**2)-4*a*c)**0.5)/(2*a)
    print(f'근은 {answer1}, {answer2}입니다.')
elif ((b**2)-4*a*c) == 0:
    common_answer = (-b+((b**2)-4*a*c)**0.5)/(2*a)
    print(f'중근은 {common_answer}입니다.')
else:
	print('실근이 존재하지 않습니다.')
```







