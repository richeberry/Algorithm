# 이코테 _ 구현 _ 문자열 재정렬

s = input()

alpha = []
num = 0

for i in s:
    if i.isdigit() == True:
        num += int(i)
    else:
        alpha += i

alpha.sort()
print(f'{"".join(alpha)}{num}')