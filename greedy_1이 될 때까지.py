# 이것이 코딩테스트다 _ Greedy 1이 될 때까지
# n이 1이 될 때까지 -1 혹은 나누는 과정을 수행해야하는 최소 횟수를 구하는 프로그램

n,k = map(int, input().split())
cnt = 0

while True:
    div = n % k # 나눌 수 있는 최대 수를 제외한 나머지
    if n % k == 0: # 바로 나누어 떨어지는 수면
        n //= k # 
        cnt += 1
    elif n == 1: # n이 1에 도달하면
        break
    else: # 나누어 떨어지지 않는 수라면
        n -= div # 나누어 떨어질 수 있는 수까지만 빼기
        cnt += div # 뺀 수 count에 더하기(한 번에 1만 뺄 수 있으므로)

print(cnt)