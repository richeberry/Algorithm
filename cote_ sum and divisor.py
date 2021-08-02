# 프로그래머스 _ 약수의 개수와 덧셈 _ 210802 (월간 코드 챌린지 시즌2)

left = 8
right = 27

# 내 코드

import time

#start = time.time()

def solution(left,right):
    def prime(n):
        return [i for i in range(1,n+1) if n%i==0]
    answer = 0
    for number in range(left, right+1):
        if len(prime(number)) %2==0:
            answer += number
        else:
            answer -= number
    return answer 

#print('time:',time.time() - start)

print(solution(left,right))


# 다른 코드

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

