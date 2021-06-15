# programmers _ 소수만들기

# prime function

n = int(input())

def prime_number(n):
    pnumber = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if pnumber[i] == True:
            for j in range(i+i, n, i):
                pnumber[j] = False

    return [i for i in range(2,n) if pnumber[i] == True]
    
print(prime_number(n))

from itertools import combinations

nums = [1,2,3,4]
numcom = list(combinations(nums, 3))
print(numcom)
sum_numcom = [sum(i) for i in numcom]
print(sum_numcom)
answer = 0
print([i for i in sum_numcom if i in prime_number(n)])

answer += len([i for i in sum_numcom if i in prime_number(n)])
print(answer)



def solution(nums):

    answer = 0
    numcom = list(combinations(nums, 3))
    sum_numcom = [sum(i) for i in numcom]
    
    n = 3000
    def prime_number(n):
        pnumber = [True] * n

        m = int(n ** 0.5)
        for i in range(2, m+1):
            if pnumber[i] == True:
                for j in range(i+i, n, i):
                    pnumber[j] = False

        return [i for i in range(2,n) if pnumber[i] == True]
    
    from itertools import combinations


    answer += len([i for i in sum_numcom if i in prime_number(n)])
    return answer
