# Inflearn _ Section 3 격자판 최대합

n = int(input())
lattice = [list(map(int, input().split())) for i in range(n)]

# 행의 합, 열의 합, 두 대각선의 합 중 가장 큰 합 출력

max_v = sum(lattice[0]) # 첫째 행의 합을 최대값을 설정
tmp = 0 # 각 합의 임시 값 저장

# 1) 행의 합
for row in lattice:
    if sum(row) > max_v:
        max_v = sum(row)

# 2) 열의 합
for i in range(n):
    max_v = max(tmp, max_v)
    tmp = 0 # 각 열의 합을 더한 후 초기화
    for j in range(n):
        tmp += lattice[j][i] 
tmp = 0

# 3-1) 왼쪽 위부터 대각선의 합
for i in range(n):
    tmp += lattice[i][i]
max_v = max(tmp, max_v)
tmp = 0

# 3-2) 오른쪽 위부터 대각선의 합
for i in range(n-1, -1, -1):
    tmp += lattice[(n-1)-i][i]
max_v = max(tmp, max_v)

print(max_v)


