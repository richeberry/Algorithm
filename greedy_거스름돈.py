# 이것이 코딩테스트다 _ Greedy 큰 수의 법칙

n = 1260
cnt = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    cnt += n // coin # 나눌 수 있는 수 까지 나눈 수(몫)을 동전 개수에 더함
    n %= coin # 다음 나눌 수는 나누고 남은 수(나머지)

print(cnt)
