# 1 번 문제
'''
Local -> Enclosed function -> Global -> Bulit-in
'''

# 2 번 문제
'''
3번
'''

# problem 3




# Workshop
# prob 1
'''
def get_secret_word(num):
    result = ''
    for i in num:
        result += chr(i)
    print(result)
get_secret_word([83, 115, 65, 102, 89])
'''

# prob 2
'''
def get_secret_number(name):
    list_name = list(name)
    result = 0
    for i in list_name:
        result += ord(i)
    print(result)
get_secret_number('john')
'''

# prob 3
'''
def get_strong_word(a, b):
    lista = list(a)
    listb = list(b)
    resulta = 0
    resultb = 0
    for i in lista:
        resulta += ord(i)
    for j in listb:
        resultb += ord(j)
    if resulta > resultb:
        print(a)
    elif resultb> resulta:
        print(b)
    else:
        print('두 이름의 아스키코드 숫자 합이 같습니다.')

    

get_strong_word('john', 'nojh')
'''


