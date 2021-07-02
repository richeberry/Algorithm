# 문자열 내림차순으로 배치하기

s = "Zbcdefg"

print(s)
slist = list(s)
slist.sort(reverse=True)
print(''.join(slist))

def solution(s):
    slist.sort(reverse=True)
    return ''.join(slist)


print(solution(s))


