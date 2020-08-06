
#T = int(input())
#for test_case in range(1, T + 1):

test_list = list(map(str, input()))
l = len(test_list)
for i in range(0, l):
    ac = ord(test_list[i]) - 64
    print(ac, end=' ')