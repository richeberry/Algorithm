# 이것이 코딩테스트다 _ 구현 게임 개발

n,m = map(int, input().split())
x,y,see = map(int, input().split())

mat = [list(map(int, input().split())) for i in range(n)]
moves = [[-1,0],[0,-1],[1,0],[0,1]] # 북 동 남 서

now = [x-1,y-1] # index
cnt = 1

while True:
    if see > 3:
        see = 0

    tmp = [x+y for x,y in zip(now, moves[see])] # 바라보는 방향으로 이동했을 때의 위치

    if min(tmp) >= 0 and max(tmp) < m: # 바라보는 방향의 칸이 맵 안의 칸이고
        if mat[tmp[0]][tmp[1]] == 1: # 그 칸이 육지라면
            now = tmp # 그 칸으로 이동 
            mat[tmp[0]][tmp[1]] += 1 # 이미 이동한 칸이므로 2로 변경 (다시 오지 않기 위해)
            cnt += 1
            see = 0 # 바라보는 방향 리셋
        elif mat[tmp[0]][tmp[1]] != 1: # 그 칸이 방문한 칸이거나 바다라면
            break
        else:
            see += 1
    else:
        see += 1

print(cnt)