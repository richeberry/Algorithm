
# Inflearn _ Section 3 _ 봉우리

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, -1, 0]

# 지도 가장자리에 0 초기화
array.insert(0,[0] * n) # 0번째 행에 [0] * n 삽입
array.append([0] * n) # 마지막 행에 [0] * n 추가

for row in array:
    array.insert(0, 0) # 행 처음에 0 삽입
    array.append(0) # 행 마지막에 0 추가

cnt = 0 # 봉우리 개수 초기화

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(array[i][j] > array[i+dx[k]][k+dy[k]] for k in range(4)): # all_조건이 모두 맞으면 참
            cnt += 1

print(cnt)
