def soluion(answers):
    answer = []
    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0,0,0]

    for idx, i in enumerate(answers):
        print(i, i % len(su1))
        if i == su1[i % len(su1)]: #i % len(su1) : 자리수 맞추려고
            count[0] += 1
        if i == su2[idx % len(su2)]:
            count[1] += 1
        if i == su3[idx % len(su3)]:
            count[2] += 1

    for i in range(len(count)):
        if max(count) == count[i]:
            answer.append(i+1) # count에는 0,1,2 이렇게 저장되니깐
    return answer