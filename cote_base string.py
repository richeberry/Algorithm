# 문자열 다루기 기본

s = 'a235'

# 내 풀이
def solution(s):
    if len(s)==4 or len(s)== 6:
        return True if s.isdigit() == True else False
    else: return False


# 다른 풀이

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


print(solution(s))
print(alpha_string46(s))

a = '3i92'
def practice(a):
    return s.isdigit() and len(s) in (4,6)
