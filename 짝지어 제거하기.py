# 프로그래머스 _ Lv 2 _ 짝지어 제거하기


def solution(s):
    # 문자를 저장할 리스트 초기화
    stack = []
    for i in s:
        # 리스트에 아무 문자도 없으면
        if len(stack) == 0:
            # 문자 추가하기
            stack.append(i)
        # 바로 전의 문자가 현재 문자와 같으면
        elif stack[-1] == i:
            # 전 문자 제거
            stack.pop()
        else:
            stack.append(i)
    # 연속되는 문자열을 담은 리스트가 0이면 전부 연속이므로
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer
