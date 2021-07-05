# 음양 더하기

absolutes = [4,7,12]
signs = [True,False,True]

# 내 풀이


def solution(absolutes, signs):
    answer = []
    for i in zip(absolutes, signs):
        if i[1] == True:
            answer.append(i[0])
        else:
            answer.append(i[0] * -1)
    return sum(answer)

print(solution(absolutes, signs))


# 다른 풀이

def solutions(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

print(solutions(absolutes, signs))

