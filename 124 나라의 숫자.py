# Programmers _ Lv.2 124 나라의 숫자


def solution(num):
    answer= ''
    while num: 
        if num % 3: # num이 3의 배수가 아니면 
            answer += str(num%3) # 3진법으로 1의 자리수부터 answer에 넣어줌
            num //= 3 # num은 3으로 나눈 몫
        else:
            answer += "4" # num이 3의 배수이면 마지막 자리수는 무조건 4가 되고, 
            num = num//3 - 1 # 마지막의 앞자리수는 -1이 된다
    return answer[::-1] # 거꾸로 더해줬으므로 뒤집어서 출력

print(solution(9))