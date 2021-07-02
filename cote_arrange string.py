# 문자열 내 마음대로 정렬하기

strings = ["abce", "abcd", "cdx"]
n = 2

# 틀린 내 풀이

def solution(strings, n):
    letters = []
    answer = []
    for word in strings:
        letters.append(word[n])
    letters.sort()
    for i in letters:
        for word in strings:
            if i == word[n]:
                answer.append(word)
    return answer

# 다른 풀이

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
