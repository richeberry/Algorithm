# Programmers Lv.2 _ H-index

def solution(citations):
    citations.sort() # 오름차순 정렬
    for idx, c in enumerate(citations): 
        if c >= len(citations) - idx:
            # c=h번 이상 인용된 논문
            # c가 c개 있거나 c개보다 많으면 (오름차순이므로 c부터 논문의 개수)
            return len(citations) - idx # 인용된 논문 수 출력
    return # 0 인용된 논문이 없고 전부 0이면 0 출력 