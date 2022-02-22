# 프로그래머스 LV.3 _ N개의 표현


def solution(N, number):
    dp  =[set([N*int('1'*i)]) for i in range(1, 9)]  # N을 i번 사용해서 나타낼 수 있는 수의 집합 ex) N,NN,NNN..
    for i in range(1,9):
        dp.append(int(str(N)*i))
    for i in range(8):
        for j in range(i):
            for x in dp[j]: # i번 사용해서 나타내는 수들
                for y in dp[i-j-1] : # N-i번 사용해서 나타낼 수 있는 수
                    dp[i].add(x - y) # 연산을 통해 나타낼 수 있는 조합 더하기
                    dp[i].add(x + y)
                    dp[i].add(x * y)
                    if y != 0: # 0을 나누면 에러남
                        dp[i].add(x // y)
                    
        if number in dp[i]: 
            print(dp)
            # N을 i번 사용해서 나타낼 수 있는 수가 dp[i]에 딕셔너리로 저장됨
            # 그 집합 안에 number가 있으면 그 집합의 인덱스+1 출력
            return i+1


    return -1