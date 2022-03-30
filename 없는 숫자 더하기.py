# Programmers _ Lv.1 없는 숫자 더하기

def solution(numbers):
    origin = [i for i in range(0,9+1)]
    numbers.sort()
    answer = 0
    for i in origin:
        if i in numbers:
            continue
        else:
            answer += i
    return answer

# 다른 풀이

def solution(numbers):
    return 45 - sum(numbers)