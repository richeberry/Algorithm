def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''

    for i in len(completion):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant)-1]