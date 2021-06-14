# 시저 암호
'''
def solution(s,n):
    answer = []
    for i in s:
        cha = chr(ord(i)+n)
        answer.extend(cha)
    return ''.join(answer)


print(solution('ab',2))
'''
'''
def solution(s,n):
    answer = ''
    for i in s:
        if i != ' ':
            num = ord(i)+n
            if 65 <= ord(i) >= 90:
                if num > 90:
                    num -= 26
                cha = chr(num)
            elif num > 122:
                num -= 26
                cha = chr(num)
            answer += cha
        else:
            answer += cha
    
    return ''.join(answer)

print(solution('AB',1))

'''


def solution(s,n):
    answer = ''
    for i in s:
        cha = ord(i) + n
        if 65 <= ord(i) <= 90:
            if cha > 90:
                answer += chr(cha-26)
            else:
                answer += chr(cha)
        elif 97 <= ord(i) <= 122:
            if cha > 122:
                answer += chr(cha-26)
            else:
                answer += chr(cha)
        if i == ' ':
            answer += ' '
    return answer

print(solution('ZzYy',1))


#다른 풀이

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)