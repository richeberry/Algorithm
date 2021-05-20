n,k = map(int,input().split())
answer = 0
for i in range(1,n+1):
    if n % i == 0:
        answer += 1
    if answer == k: # 슬라이싱 말고 발견하면 그냥 출력
        print(i)
        break
else: #for문이 정상적으로 끝났다면 else로 안 옴 없을 때만 else로 옴
    print(-1)