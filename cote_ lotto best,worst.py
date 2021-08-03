# 프로그래머스 _ 로또의 최고 순위와 최저 순위 _ 210803

lottos = [0, 0, 0, 0, 0, 0]				
win_nums = [38, 19, 20, 40, 15, 25]				
answer = [0,0] # 맞춘 개수 best, worst 

# 내 풀이
def solution(lottos, win_nums):
    answer = [0,0]
    for idx, num in enumerate(win_nums):
        if num in lottos:
            answer[0] += 1
            answer[1] += 1
    
    answer[0] += int(lottos.count(0))

    for i in range(len((answer))):
        answer[i] = 6-(answer[i])+1
        if answer[i] > 5:
            answer[i] = 6
    return answer


# 다른 풀이

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]