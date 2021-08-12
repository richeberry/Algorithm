# 프로그래머스 _ 타겟 넘버 _ 210812


numbers = [1,1,1,1,1]
target = 3


from collections import deque

# deque를 이용한 BFS 풀이
'''
def solution(numbers, target):
    answer = 0
    deqnum = deque()
    n = len(numbers)
    deqnum.append([numbers[0],0])
    deqnum.append([-1*numbers[0],0])
    print(deqnum)
    while deqnum:
        tmp, idx = deqnum.popleft()
        idx += 1
        if idx < n:
            deqnum.append([tmp+numbers[idx], idx])
            deqnum.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer


print(solution(numbers,target))


# 재귀함수를 이용한 DFS 풀이

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer




#BFS 이용한 풀이
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

    '''


# BFS 풀이

def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    return sup.count(target)

'''
def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        print('i:',i)
        for j in sup:
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
        print('sup:',sup)
    return sup.count(target)

print(solution(numbers, target))

'''

def solution(numbers, target):
    start = [0]
    for num in numbers:
        tmp = []
        for i in start:
            tmp.append(i+num)
            tmp.append(i-num)
        start = tmp
    answer = start.count(target)
    return answer


# recursion_ 꼭 이해 완벽히하고 외우기

def solutions(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0])
        +solution(numbers[1:], target+numbers[0])


