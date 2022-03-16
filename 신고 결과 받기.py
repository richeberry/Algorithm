# Programmers _ Lv.1 신고 결과 받기 2022 KAKAO BLIND RECRUITMENT

def solution(id_list, report, k):
    report = list(set(report))
    ban= [[] for _ in range(len(id_list))] # 신고한 아이디들 id_list 순으로
    banned = [0 for _ in range(len(id_list))] # 신고 당한 아이디들 횟수 id_list 순으로
    result = [0] * len(id_list) # 신고한 아이디중 정지된 아이디

    for id in report:
        a = id.split(' ')

        whereban = id_list.index(a[0]) #id_list 순서대로 신고한 아이디 인덱스 받아옴
        ban[whereban].append(a[1])

        wherebanned = id_list.index(a[1]) # 신고 당한 아이디 인덱스 받아옴 
        banned[wherebanned] += 1

    for idx, id in enumerate(ban):
        for i in id:
            where = id_list.index(i) # id_list의 인덱스 가져와서
            if banned[where] >= k: # 신고당한 아이디 리스트의 인덱스가 k값보다 크면 
                result[idx] += 1 # result에 + 1

    return result



# 다른 풀이

'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

'''