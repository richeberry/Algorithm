# Programmers _ Lv.2 124 나라의 숫자

def solution(num):
    answer = ''
    while num:
        if num % 3:
            answer += str(num%3)
            num //= 3
        else:
            answer += "4"
            num = num//3 -1
    return answer[::-1]