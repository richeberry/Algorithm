# programmers_콜라츠 추측_210601

#https://programmers.co.kr/learn/courses/30/lessons/12943


# Algorithm

num = 6 #answer = 8
#num = 16 #answer = 4
#num = 626331 #answer = -1
def solution(num):
    answer = 0
    while num > 1:
        if num%2==0:
            num /= 2
        elif num%2 == 1:
            num = (num*3)+1
        answer += 1
    if answer >= 500:
        answer = -1
    return answer

print(solution(num))

def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

print(collatz(6))
