# 키패드 누르기 _ 210707


'''
pad = [[1,4,7],[2,5,8],[3,6,9]]

for num in numbers:

    if num == pad[0]: # Left
        answer += 'L'
        last_l = num
    elif num == pad[2]: # Right
        answer += 'R'
        last_r = num
    else: # Middle'
        num = 11 if num == 0 else num
        abs_l = abs(num-last_l)
        abs_r = abs(num-last_r)

        if sum(divmod(abs_l, 3)) > sum(divmod(abs_r, 3)):
            answer += 'R'
            last_r = num
        elif sum(divmod(abs_l, 3)) < sum(divmod(abs_r, 3)):
            answer += 'L'
            last_l = num
        else:
            if hand == 'left':
                answer += 'L'
                last_l = num
            else:
                answer += 'R'
                last_r = num
        

print(answer)

'''

# 내 풀이

def solution(numbers, hand):
    answer = ''
    last_l = 10
    last_r = 12
    
    pad = [[1,4,7],[2,5,8],[3,6,9]]

    for num in numbers:
        if num in pad[0]: # Left
            answer += 'L'
            last_l = num
        elif num in pad[2]: # Right
            answer += 'R'
            last_r = num
        else: # Middle'
            num = 11 if num == 0 else num

            abs_l = abs(num-last_l) # 거리 계산하기 위해
            abs_r = abs(num-last_r)

            if sum(divmod(abs_l, 3)) > sum(divmod(abs_r, 3)):
                answer += 'R'
                last_r = num
            elif sum(divmod(abs_l, 3)) < sum(divmod(abs_r, 3)):
                answer += 'L'
                last_l = num
            else:
                if hand == 'left':
                    answer += 'L'
                    last_l = num
                else:
                    answer += 'R'
                    last_r = num
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

print(solution(numbers,hand))