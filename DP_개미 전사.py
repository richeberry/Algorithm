# 이코테 _ DP 개미 전사

# 정수 n 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 100

# DP 진행 (바텀업)
dp[0] = array[0]
dp[1] = max(array[0],array[1])

for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2] + array[i]) # 0부터 n까지 모든 경우의 수를 하나씩 더해서 최종 최댓값 수 출력


print(dp[n-1])