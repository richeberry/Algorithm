# 자연수 뒤집어 배열로 만들기


'''def solution(n):
    answer = []
    if n<=0: return
    answer.append(n%10)
    answer = solution(n//10)
    print(answer)
    return list(map(int, answer))
'''

n = 12345
n = list(map(int, reversed(str(n))))
print(n)

def solution(n):
    return list(map(int, reversed(str(n))))