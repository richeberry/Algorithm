# 그리디 _ 곱하기 혹은 더하기
# 무조건 왼쪽에서 오른쪽으로 계산

s = input()
result = 0

for i in s:
    if int(i) == 0 or int(i) == 1: # 0이나 1일 땐 더하기
        result += 0
    elif result == 0: # 아직 저장 값이 0이면 더하기
        result += int(i)
    else: # 그 외 곱하기
        result *= int(i)

print(result)
