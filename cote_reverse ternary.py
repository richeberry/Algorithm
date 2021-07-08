# 3진법 뒤집기 _ 210706


n = 45
num = ''
answer = 0

while n>0:
    n, mod = divmod(n,3)
    num += str(mod)
    #print(n,mod)
#print(num)
for idx, i in enumerate(num):
    answer += int(i)*(3**(len(num)-(idx+1)))

print(answer)

# 내 풀이
def solution(n):
    num = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n, 3)
        num += str(mod)
    for idx, i in enumerate(num):
        answer += int(i) * (3 ** (len(num) - (idx + 1)))
    return answer

# 다른 풀이

def solutions(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer