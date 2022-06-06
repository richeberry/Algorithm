# Inflearn _ Section 3 탐색 & 시뮬레이션 _ 곶감(모래시계)

from collections import deque

n = 5 # n * n 만들 숫자 입력 받음
mat = [list(map(int, input().split())) for _ in range(n)] # 2차원 배열 생성
m = int(input())

# 회전하기
for i in range(m):
    row, direction, num = map(int, input().split()) # 회전할 행, 방향, 칸 수 입력 받음
    now = deque(mat[row-1]) # 회전할 행을 데크로 만듦
    if direction == 0: # 방향이 0이면 왼쪽으로 칸 수 만큼 회전
        now.rotate(-num)
    else: # 방향이 1이면 오른쪽으로 칸 수 만큼 회전
        now.rotate(num) 
    mat[row-1]=list(now) # 배열에 반영

# 감 개수 세기
persi = 0 # 감 개수 
s = 0 # 앞 뒤 슬라이싱 할 숫자
for i in range(n):
    if i <= n//2: # 첫 행부터 감 개수가 한 행에서 1이 되는 행까지
        persi += sum(mat[i][s:n-s])
        s += 1
    
    else:
        s -= 1 # 감 개수가 1인 행의 다음 행부터 마지막 행까지
        persi += sum(mat[i][s-1:n-s+1])

print(persi)