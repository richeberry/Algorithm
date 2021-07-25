# 실패율 _ fail rate _ 210709 


n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3] 


import fractions
'''
for i in range(1,n+1):
    tmp = stages.count(i)
    print('i:',i)
    print('tmp:',tmp)
    eq = fractions.Fraction(tmp,(len(stages)-(last_tmp<i)))
    print('eq:',eq)
    last_tmp = tmp
    print('last_tmp:',last_tmp)
'''

'''
from collections import Counter
fail = []
count = Counter(stages)
keys = count.keys()
items = count.items()
print('count:',count)
print('keys:',keys)
print('items:',items)
'''
# 다른 풀이

def solution(n, stages):
    answer = []
    fail_per = {}
    stage_people = len(stages)
    for i in range(1, n+1):
        count = stages.count(i) # 1부터 n+1까지 순서대로 count(i) 출력
        print(count)
        if stage_people == 0: # 스테이지에 도전한 사람이 0이면 실패율 0
            fail_per[i] = 0
        else: #실패율 : 스테이지에 도전중인 사람 / 스테이지에 도달한 사람 수 
            fail_per[i] = count/ stage_people
            print('fail_per:',fail_per[i])
        
        stage_people = stage_people - count # 스테이지에 도달한 사람 수 - i의 개수
    print(fail_per)
    answer = [stage[0] for stage in sorted(fail_per.items(), key = lambda x: (-x[1],x[0]))]
    return answer 
    
print(solution(n,stages))