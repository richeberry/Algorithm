# 프로그래머스 _ 숫자 문자열과 영단어 _ 210801

answer = ''
s = "one4seveneight"
stack = []

number = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

# 내 풀이 (하다 망함)
for i in s:
    if i.isalpha():
        stack += i
        if "".join(stack) in number.values():
            answer += number.keys["".join(stack)]
    else:
        answer += i


# 다른 풀이

def solution(s):
    number = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    for item in number.items():
        s = s.replace(item[1], str(item[0]))
    return int(s)


# 다른 풀이 2

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
