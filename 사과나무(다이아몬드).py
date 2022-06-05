
# Inflearn _ Section 3 _ 사과나무(다이아몬드)

# 내 풀이
n = int(input())
apples = [list(map(int, input().split())) for _ in range(n)] # 2차원 배열로 N * N 받기
get = 0
for i in range(n):
    if i <= n//2: # 다이아몬드 윗부분
        get += sum(apples[i][(n // 2) - i:(n // 2) + i+1]) # 차례로 홀수 만큼 늘어남

    else: # 다이아몬드 아래부분
        get += sum(apples[i][- (n + n // 2) + i:(n // 2) - i]) # 차례로 홀수 만큼 줄어듦
print(get)


# 인프런 풀이

a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1