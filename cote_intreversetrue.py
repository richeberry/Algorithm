#숫자 큰 순서대로 배열


# 단순히 숫자 거꾸로
'''
def solution(n):
    if n <=  0 : return
    print(n%10, end = '')
    return solution(n//10)
'''



def solution(n):
    n = list(str(n))
    answer = sorted(n, reverse=True)
    return int("".join(answer))
