
# programmers _ 부족한 금액 계산하기 

def solution(price, money, count):
    n = 0
    while count >= 0: # count가 0이 될 때까지 
        n += price*count # 모든 요금을 더함
        count -= 1 # 요금을 더하면 count에서 1씩 빼주어 줄어든 요금으로 만들기
    if (money-n) >= 0: # 금액이 부족하지 않으면
        return 0
    else:
        return abs(money-n) # 부족하면 필요한 차액 절대값으로 출력