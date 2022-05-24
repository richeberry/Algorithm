
# Inflearn _ Section 3 수들의 합

n, m = map(int, input().split())
lst = list(map(int, input().split()))

tmp = 0
cnt = 0

i = 0
while True:
    tmp += lst[i]
    i += 1
    if tmp > m:
        lst.pop(0)
        tmp = 0
        i = 0
    elif tmp == m:
        cnt += 1
        tmp = 0
        i = 0
        lst.pop(0)

    elif i >= len(lst):
        break

print(cnt)