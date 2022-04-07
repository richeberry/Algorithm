# 이것이 코딩테스트다 _ 구현 시각
# 모든 경우의 수를 합해도 86400 이므로 100,000 이하는 ONlogN 가능
# 시간 제한이 2초이므로 O(N^3)으로 풀 수 있다.


h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)