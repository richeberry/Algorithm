# Programmers _ 2019 카카오 인턴십 _ 튜플

# 내 풀이
def solution(s):
    data = [[] for _ in range(len(s))] # 숫자를 넣을 리스트 초기화

    s = s[1:len(s)-1] # 어차피 집합의 모임이므로, 제일 바깥 괄호 제거
    num = '' # 임시 숫자를 담을 변수
    answer = [] # 정답을 담을 변수

    for i in range(len(s)):
        if s[i] == '{': # {이면 임시 숫자 시작
            now = i
            flag = True
        elif s[i].isdecimal(): # 숫자이면
            num += s[i] # 임시 숫자에 저장
        elif s[i] == ',': # ,가 나오면 같은 리스트 내 다른 숫자인지, 다른 집합인지 구별
            if flag == True: # 같은 리스트 내 다른 숫자이면
                data[now].append(num) # now와 같은 리스트에 더하기
                num = '' # 임시 숫자 초기화
        elif s[i] == '}': # 임시 숫자 입력 끝
            data[now].append(num)
            num = ''
            flag = False

    data.sort(key=len) # 원소 수대로 정렬

    for i in range(len(data)): # 빈 리스트 제거
        if len(data[i]) > 0:
            data = data[i:] # 빈 리스트들 삭제
            break

    for i in data:
        for num in i:
            if int(num) not in answer: # 원소 길이가 1인 리스트부터 하나씩 더해져가며 집합이 생기므로, 중복 제거하여 튜플 만들기
                answer.append(int(num))

    return answer

# 다른 풀이
'''
import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
'''