# 이코테 _ 그리디 _ 모험가 길드

n = int(input())
guild = list(map(int, input().split()))

guild.sort() # 오름차순으로 정렬 _ 작은 공포도부터 팀을 만들어야 최대 팀을 만들 수 있으므로
group = [] # 임시로 그룹을 만드는 변수 초기화
team = 0 # 전체 팀 개수 저장할 변수 초기화

for idx, i in enumerate(guild):
    group.append(guild[idx]) # 임시 그룹에 현재 공포도 저장
    if len(group) == i: # 현재 공포도와 임시 그룹의 인원 수가 같으면
        team += 1 # 전체 팀 + 1
        group = [] # 임시 그룹 초기화

print(team)