# Programmers _ Lv.1 나머지가 1이 되는 수 찾기

def solution(n, i=1):
    while True:
        if n % i == 1:
            break
        i += 1
    return i