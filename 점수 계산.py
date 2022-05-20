# Inflearn _ 점수 계산

n = int(input())
score_lst = list(map(int, input().split())) # 한 줄에 맞은 점수와 틀린 점수 받기
now = 0 # 현재 맞은 점수가 몇 번째인지 저장
score = 0 # 최종 점수 저장
for i in score_lst:
    if i == 1: # 맞았으면
        now += 1 # 현재 점수 + 1
        score += now # 최종 점수에 현재 점수 더함
    else: # 틀렸으면
        now = 0 # 초기화

print(score)
