# 이코테 _ DFS 음료수 얼려 먹기

n,m = map(int, input().split())

mat = [list(map(int, input())) for i in range(n)]

def dfs(x,y):
    # 범위를 벗어나면 종료
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문하지 않은 노드라면
    if mat[x][y] == 0:
        # 노드 방문
        mat[x][y] = 1
        # 인접한 노드 상 하 좌 우 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False 

# 모든 위치에 대하여 음료수 채우기 
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 
        if dfs(i,j) == True:
            result += 1

print(result)
