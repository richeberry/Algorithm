dartresult = '1S*2T*3S'

dartresult = dartresult.replace('10', 'A')
tmp = []
bonus = {'S':1, 'D':2, 'T':3}
option = {'*':2, '#':-1}

for dart in dartresult:
    if dart.isdigit() or dart == 'A':
        tmp.append(10 if dart == 'A' else int(dart))
    elif dart in ('S', 'D', 'T'):
        last = tmp.pop()
        tmp.append(last ** bonus[dart])
    elif dart == '#':
        tmp[-1] *= option[dart]
    elif dart == '*':
        last = tmp.pop()
        if len(tmp):
            tmp[-1] *= option[dart]
        tmp.append(last * option[dart])
    print('dart', dart)
    print('tmp', tmp)
    