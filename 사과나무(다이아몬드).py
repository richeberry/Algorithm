
# Inflearn _ Section 3 _ 사과나무(다이아몬드)

n = int(input())
apples = [list(map(int, input().split())) for i in range(n)] # 2차원 배열로 N * N 받기
get = 0
for i in range(n):
    if i <= n//2: # 다이아몬드 윗부분
        get += sum(apples[i][(n // 2) - i:(n // 2) + i+1]) # 차례로 홀수 만큼 늘어남

    else: # 다이아몬드 아래부분
        get += sum(apples[i][- (n + n // 2) + i:(n // 2) - i]) # 차례로 홀수 만큼 줄어듦
print(get)