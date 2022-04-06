# 이것이 코딩테스트다 _ greedy  숫자 카드 게임

n,m = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(n)]

for i in mat: # 한 행에서 가장 작은 수가 큰 행을 선택하여, 가장 작은 수 출력 
    now = min(i) # 행에서 가장 작은 수 선택
    result = max(now, min(i)) # 전 행의 가장 작은 수와 비교

print(result)