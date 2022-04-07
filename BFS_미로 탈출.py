# 이코테 _ BFS 미로 탈출

from collections import deque

n,m = map(int, input().split())
mat = [list(map(int, input())) for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1] # 상, 하, 좌, 우

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft() # (0,0)시작
        
        for i in range(4): # 현재 위치에서 네 방향 (상 하 좌 우) 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 범위를 넘어간 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있으면 무시
            if mat[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우 최단 거리 기록
            if mat[nx][ny] == 1: # 괴물이 없을 경우
                mat[nx][ny] = mat[x][y] + 1 # 이동할 위치에 지금까지 이동한 거리 더하기
                queue.append((nx,ny)) # 이동한 칸부터 다시 시작
    return mat[n-1][m-1] # 무조건 n,m 위치가 출구이므로 지금까지 더한 거리 return

print(bfs(0,0))
