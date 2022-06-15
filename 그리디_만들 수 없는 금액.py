# 이코테 _ 그리디 _ 만들 수 없는 금액


# 내 풀이

n = int(input())
# 동전 리스트로 받기
coin = list(map(int, input().split()))
# 오름차순으로 정렬
coin.sort()

# 만들 수 있는 금액 리스트 만들기
mixcoin = []

for idx, i in enumerate(coin):
    # 조합할 동전 첫번째부터 차례대로
    tmpcoin = i
    # 만들 수 있는 금액 리스트에 없으면 추가
    if i not in mixcoin:
        mixcoin.append(i)
    # 만들 수 있는 금액 첫 번째 동전 다음 동전들과 조합하기
    for j in coin[idx+1:]:
        tmpcoin += j
        # 만들 수 있는 금액 리스트에 없으면 추가
        if tmpcoin not in mixcoin:
            mixcoin.append(tmpcoin)

mixcoin.sort()

# 1부터 만들 수 있는지 검사하고 없으면 출력
for i in range(1, len(mixcoin)+1):
    if i != mixcoin[i-1]:
        print(i)
        break


