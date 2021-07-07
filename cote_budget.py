# 프로그래머스 _ 예산 210702

d= [1,3,2,5,4]
budget = 9
'''
from itertools import combinations

combi_lists = []
answer = 0
for idx, i in enumerate(d):
    combi_list = list(combinations(d,len(d)-idx))
    print(combi_list)
    for j in combi_list:
        if sum(j) <= budget:
            combi_lists.append(len(j))

print(combi_lists)
answer = max(combi_lists)
print(answer)
'''

# 내 풀이 1 (틀린 풀이_시간 초과)
'''
def solution(d, budget):
    from itertools import combinations
    combi_lists = []
    answer = 0
    for idx, i in enumerate(d):
        combi_list = list(combinations(d,len(d)-idx))
        for j in combi_list:
            if sum(j) <= budget:
                combi_lists.append(len(j))
                
    return max(combi_lists)


print(solution(d,budget))
'''


# 다른 풀이 1

def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(len((d))):
        if sum(d[:i+1]) <= budget:
            answer += 1
    return answer 


# 다른 풀이 2

def solutionss(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

print(solutionss(d,budget))

