# 이것이 코딩테스트다 _ Greedy 큰 수의 법칙


n,m,k = map(int, input().split())
lst = list(map(int, input().split()))

nums = [lst.pop(lst.index(max(lst))) for i in range(2)] # 제일 큰 수와 그 다음으로 큰 수만 사용하므로 따로 저장

result = 0 # 더해진 출력 값 
cnt = 0 # 더할 수 있는 횟수

while True:
    result += nums[0] # 연속해서 더할 수 있는 횟수까지 더함 
    cnt += 1 # 더한 횟수 추가

    if cnt % k == 0 : # 연속해서 더할 수 있는 횟수가 되면 
        result += nums[1] # 두 번째로 큰 수 더함 
        cnt += 1 # 더한 횟수 추가 

    elif cnt == m: # 더할 수 있는 최대 횟수에 도달하면 
        break # 탈출

print(result)
