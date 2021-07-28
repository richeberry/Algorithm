# 프로그래머스 _ 다트 게임 210724

dartresult = '1S*2T*3S'
dartresult = dartresult.replace('10','A')
tmp = []

bonus = {'S': 1, 'D': 2, 'T': 3}
option = {'*': 2, '#': -1}

# 내 풀이

def solution(dartresult):
    dartresult = dartresult.replace('10','A')
    tmp = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1}

    for dart in dartresult:
        if dart.isdigit() or dart == 'A': # 숫자인지 판별
            tmp.append(10 if dart == 'A' else int(dart)) #숫자일 때
        elif dart in ('S','D','T'): #SDT
            last = tmp.pop()
            tmp.append(last ** bonus[dart])
        elif dart == '#':
            tmp[-1] *= option[dart] # lastnumber * -1
        elif  dart == '*':
            last = tmp.pop()
            if len(tmp): # if len(tmp) is not 0
                tmp[-1] *= option[dart] #lastnumber * 2
            tmp.append(last * option[dart])
    return sum(tmp)

print(solution(dartresult))


# 다른 풀이

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer