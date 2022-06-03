# 이것이 코딩테스트다 _ 구현 상하좌우
# 7분

# 내 풀이
n = int(input())
plan = list(map(str, input().split()))

now = [1,1]

for i in plan:
    if i == 'L':
        if now[1] > 1:
            now[1] -= 1
    elif i == 'R':
        if now[1] < n:
            now[1] += 1
    elif i == 'U':
        if now[0] != 1:
            now[0] -= 1
    elif i == 'D':
        if now[0] != n:
            now[0] += 1

print(now)


# 책 풀이
n = int(input())
plans = input().split()
x,y = 1,1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx, ny

print(x,y)