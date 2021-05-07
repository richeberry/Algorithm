def solution(s):
    s = len(s)
    ss = s[:-4]
    num = s[-4:]
    return '*'*(s-4)+num

def solution(phone_number):
    front = phone_number[:-4]
    back = phone_number[-4:]
    return (len(front)*'*')+back



print(solution('0122776530'))