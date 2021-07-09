# 프로그래머스 programmers _ 내적 inner product _ 210708


a = [-1,0,1]
b = [1,0,-1]

# 내 풀이
def solution(a,b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer 


# 다른 풀이 1
solution = lambda x, y: sum(a*b for a, b in zip(x, y))

# 다른 풀이 2

def solution(a, b):
    return sum(map(lambda i: a[i]*b[i], range(len(a))))
