# 문자열 내 p와 y의 개수


s = "pPyY"

# 내 풀이 - 하나하나 비교했다는 것..^^
def solution(s):
    panswer = 0
    yanswer = 0
    slist = list(s.upper())
    for i in range(len(slist)):
        if slist[i] == 'P':
            panswer += 1
        elif slist[i] == 'Y':
            yanswer += 1
    return True if panswer == yanswer else False

#print(solution(s))

# 다른 풀이

def numPY(s):
    return s.lower().count('p') == s.lower().count('y')


print(numPY(s))