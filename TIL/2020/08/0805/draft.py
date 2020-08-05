'''
2 7 4 3 6
8 5 8 3 2
2 2 3 6 9
5 9 2 5 7
3 6 2 9 4
'''
import copy
arr = []
for i in range(5):
    arr += [list(map(int, input().split()))]
arr_copy = copy.deepcopy(arr)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(5):
    for j in range(5):
        result = 0
        for k in range(4):
            temp = 0
            nx = j + dx[k]
            ny = i + dy[k]
            print(nx, ny)
            if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                temp += 0
            else:
                temp = abs(arr[ny][nx] - arr[i][j])
            result += temp
        arr_copy[i][j] = result
print(arr_copy)
print(arr)


