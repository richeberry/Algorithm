# x만큼 간격이 있는 n개의 숫자


def solution(x,n):
    if x > 0:
        answer = list(range(x,(x*n)+int(x/x),x))
    elif x == 0:
        answer = [x]*n
    elif x < 0:
        answer = list(range(x,(x*n)-int(x/x),x))
    return answer
        
print(solution(0,3))


# 0을 고려하지 않은 코드
'''def solution(x,n):
    return list(range(x,(x*n)+int(x/x),x)) if x>=0 else list(range(x,(x*n)-int(x/x),x))
'''
