# 프로그래머스 _ 폰켓몬 210729
import time

nums = [3,1,2,3]
#nums = [3,3,3,2,2,4]	
#nums = [3,3,3,2,2,2]	


# 내 풀이 

def solution(nums):
    n = len(nums)//2
    nums = list(set(nums))
    return n if len(nums) > n else len(nums)

print(solution(nums))
'''
# 시간초과 된 코드 2
start_time = time.time()
def solution(nums):
    from itertools import combinations as cb
    tmp = []
    n = len(nums)//2
    nums = list(set(nums))
    if len(nums) < n:
        picks = list((cb(nums, len(nums))))
    else:
        picks = list(((nums, n)))
    [tmp.append(len(set(pick))) for pick in picks]
    return(max(tmp))

print(solution(nums))

end_time = time.time()
print('time:', end_time - start_time)

# 시간초과 된 코드 1


start_time = time.time()

def solution(nums):
    from itertools import combinations
    tmp = []
    picks = list((combinations(nums,int(len(nums)/2))))
    [tmp.append(len(set(pick))) for pick in picks]
    return(max(tmp))

print(solution(nums))

end_time = time.time()
print('time:', end_time - start_time)

'''



# 다른 풀이

def solution(ls):
    return min(len(ls)/2, len(set(ls)))
