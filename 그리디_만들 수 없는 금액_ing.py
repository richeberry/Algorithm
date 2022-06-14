# 그리디 _ 만들 수 없는 금액

# n = int(input())
n = 5
# coin = list(map(int, input().split()))
coin =[3, 2, 1, 1, 9]

print(coin)
coin.sort()

mixcoin = []

for i in coin:
    for j in coin:
        print(i, j, i+j)
        if i+j in mixcoin:
            continue
        else:
            mixcoin.append(i+j)
mixcoin.sort()
print(mixcoin)


