# Inflearn_정다면체

'''
li = [4, 6, 8, 12, 20]
n,m = random.sample(li,2)
'''
max = 0
n,m = map(int, input().split())
cnt = [0]*(n+m+1) #눈의 합

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j] += 1 #i와 j가 눈, cnt[i+j] 눈의 합 - 을 1씩 증가
for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max: #눈의합이 max이면
        print(i, end=' ')

