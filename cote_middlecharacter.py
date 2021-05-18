# 가운데 글자 가져오기




def solution(s):
    answer = ''
    print(s)
    if len(s) % 2 != 0 :
        answer = s[int((len(s)+1)/2)-1] # 정수가 아니면 TypeError: string indices must be integers 오류가 발생한다
    elif len(s) % 2 == 0:
        answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
    return answer

print(solution('HappyMonday'))


# 다른 풀이

def string_middle(str):
    return str[(len(str) - 1) // 2:len(str) // 2 + 1]
