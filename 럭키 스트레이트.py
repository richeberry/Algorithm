# 이코테 _ 구현 _ 럭키 스트레이트


n = int(input())
n = str(n)
num = [0] * 2
for i in range(len(n)):
    if i < (len(n) // 2): num[0] += int(n[i])
    else:
        num[1] += int(n[i])

if num[0] == num[1]:
    print("LUCKY")
else:
    print("READY")