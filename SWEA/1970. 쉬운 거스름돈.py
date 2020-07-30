T = int(input())

for mon in range(1, T + 1):
    a = int(input())

    oman = 0
    while a >= 50000:
        a -=     50000
        oman     += 1
        
    man = 0
    while a >= 10000:
        a -= 10000
        man += 1
        
    ocun = 0
    while a >= 5000:
        a -= 5000
        ocun += 1
        
    cun = 0
    while a >= 1000:
        a -= 1000
        cun += 1
        
    obak = 0
    while a >= 500:
        a -= 500
        obak += 1
        
    bak = 0
    while a >= 100:
        a -= 100
        bak += 1
        
    osib = 0
    while a >= 50:
        a -= 50
        osib += 1
        
    sib = 0
    while a >= 10:
        a -= 10
        sib += 1
        
    print(f'#{mon}')
    print(f'{oman} {man} {ocun} {cun} {obak} {bak} {osib} {sib}')

