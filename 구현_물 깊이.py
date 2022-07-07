s = "aabbaccc"

def solution(s):
    answer = len(s)
    compressed = ''
    
    for word in range(1, len(s)//2 + 1):
        compressed = ''
        count = 1
        before = s[0:word]

        for j in range(word, len(s), word):
            if before == s[j:j+word]:
                count += 1

            else:
                compressed += str(count) + before if count >= 2 else before
                count = 1

        compressed += str(count) + before if count >= 2 else before
    
    return answer 