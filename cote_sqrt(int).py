# 정수 제곱근 판별 210530

# code 1
'''
def solution(n):
    x = list(range(1,80000))
    if n ** 0.5 in x:
        return int((n ** 0.5)+1) ** 2
    else:
        return -1
# 2,4 틀림 (정확성 88.9)


# code 2
def solutions(n):
    if n ** 0.5 / int(n**0.5) == 1:
        answer = int((n**0.5) + 1) ** 2
    else: 
        answer = -1
    return answer 
'''

# 최종 코드
def solution(n):
    return int((n**0.5) + 1) ** 2 if n ** 0.5 / int(n**0.5) == 1 else -1


