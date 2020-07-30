# prac 1
'''
class Doggy:
    
    num_of_dogs = 0
    birth_of_dogs = 0
    death_of_dogs = 0
    def __init__(self, name, breed):
        self.name = f'강아지 이름은 {name}입니다.'
        self.breed = f'강아지 견종은 {breed}입니다.'
        self.age = 1
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1

    def bark(self):
        print('멍멍')

    def get_status(self):
        print(f'현재 강아지의 숫자는 {Doggy.num_of_dogs}마리입니다.')
        print(f'지금까지 강아지는 총 {Doggy.birth_of_dogs}마리가 태어났습니다.')

    def __del__(self):
        Doggy.num_of_dogs -= 1
        Doggy.death_of_dogs += 1


d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

print(d1.name)
print(d1.breed)
d1.bark()
'''
'''
# prac 2
import random

class ClassHelper:

    def __init__(self, ls):
        self.ls = ls
    
    def pick(self, n):

        return random.sample(self.ls, n)

    def match_pair(self):
        ls2 = self.ls[:] 
        ls3 = []
        while len(ls2) != 0:
            if len(ls2) == 3:
                ls3 += [ls2[:]]
                ls2.remove(ls2[2])
                ls2.remove(ls2[1])
                ls2.remove(ls2[0])
            else:
                match = random.sample(ls2, 2)
                ls3 += [match]
                ls2.remove(match[1])
                ls2.remove(match[0])
        return ls3
        
ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피', '전싸피', '최싸피'])
print(ch.pick(2))
print(ch.match_pair())
'''
for i in range(2, -1, -1):
    print(i)
