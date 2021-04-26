

def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        re_array = array[i-1:j]
        re_array.sort()
        answer.append(re_array[k-1])

    return answer


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
