# 0730_Homeworkshop_전영제

### Homework

#### 1

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return round((self.pi * self.r * self.r), 2)
    
    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

circle_instance = Circle(3, 2, 4)

print(circle_instance.area())
print(circle_instance.circumference())
print(circle_instance.center())
```



#### 2

``` python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')
    
    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def walk(self):
        print(f'{self.name}! 달린다!')
        
    
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):

    def fly(self):
        print(f'{self.name}! 퍼더덕!')
dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```



#### 3

``` python
#ZeroDivisionError : 0으로 나누었을 때 발생
#NameError : 정의되지 않은 변수의 이름을 사용했을 때 발생
#TypeError : 해당 타입해서 사용할 수 없는 함수를 사용했을 때 발생
#IndexError : 리스트에서 없는 인덱스를 사용했을 때 발생
#KeyError : 딕셔너리에서 없는 키를 사용했을 때 발생
#ModuleNotFoundError : import하고자하는 모듈을 경로에서 찾을 수 없을때 발생
#ImportError : from에서 찾은 패키지 혹은 모듈에서 import하고자 하는 이름의 함수가 없을 때 발생
```



### Workshop

#### 1

``` python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.x1 = self.p1.x
        self.y1 = self.p1.y
        self.x2 = self.p2.x
        self.y2 = self.p2.y

    def get_area(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y2)
    
    def get_perimeter(self):
        return (abs(self.x1 - self.x2) + abs(self.y1 - self.y2)) * 2

    def is_square(self):
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)

p1 = Point(1, 3)
p2 = Point(3, 1)
rec1 = Rectangle(p1, p2)
p3 = Point(3, 7)
p4 = Point(6, 4)
rec2 = Rectangle(p3, p4)
print(rec1.get_area())
print(rec1.get_perimeter())
print(rec1.is_square())
print(rec2.get_area())
print(rec2.get_perimeter())
print(rec2.is_square())
```

