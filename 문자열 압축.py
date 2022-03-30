
# Programmers Lv.2 _ 문자열 압축 (2020 KAKAO BLIND RECRUITMENT)


def solution(s):
    answer = len(s)
    for word in range(1, len(s)//2+1): # 반복될 단어가 문자열의 두 배를 넘을 수는 없음
        # print('word',word)
        compressed = '' # 변환 단어 저장할 변수
        before = s[0:word] # s의 앞부터 word 만큼의 문자 추출 예) a, ab, aba ...
        count = 1 # 압축 수 

        for j in range(word, len(s), word): # word 크기만큼 증가 시키면서 문자열 비교
            if before == s[j:j+word]: # 앞의 글자가 현재 글자와 같으면 
                # print('if',before)
                count += 1 # 압축 수 +1
            else: # 다른 문자열이면
                # print('else',before)
                compressed += str(count) + before if count >= 2 else before #count가 2 이상이라면 compressed에 count와 함께 추가
                before = s[j:j+word] # before 초기화
                count = 1
        
        compressed += str(count) + before if count >= 2 else before # 남아있는 문자열도 동일하게
        answer = min(answer, len(compressed)) # 원래 문자열 크기와 비교 후 그중에 가장 짧은 문자열 출력
    return answer 


