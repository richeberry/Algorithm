def solution(a,b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = sum(month[:(a-1)])+(b-1)
    answer = week[day%len(week)]
    return answer

print(solution(8,1))



import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2021, a, b).weekday()]

print(getDayName(4,27))