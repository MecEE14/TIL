n = list(map(int,list(input())))
print(n)
l = len(n)
m = 0
for i in range(0, l):
    m += n[i]
print(m)