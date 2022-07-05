# 이코테 _ 구현 _ 문자열 재정렬


# 첫 번째 풀이
'''
s = input()

alpha = []
num = 0

for i in s:
    if i.isdigit() == True:
        num += int(i)
    else:
        alpha += i

alpha.sort()
print(f'{"".join(alpha)}{num}')
'''

# 두 번째 풀이

import re

s = input()
num = 0
for i in re.findall('\d',s):
    num += int(i)
s = ''.join(sorted(re.findall('\D',s)))
print(f'{s}{num}')