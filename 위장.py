# Programmers Lv.2 위장(Hash)

from functools import reduce

def solution(clothes): 
    
    clothes_dic = {} # 딕셔너리 생성
    for cloth, kind in clothes: # 리스트로 들어오는 옷들 중
        clothes_dic[kind] = clothes_dic.get(kind,0) + 1
        # clothes_dic[kind] key 값에 get을 이용하여 값을 만들어주고 
        # key값이 kind일 때마다 +1 추가 (옷 종류는 상관 없으니까)
    print(clothes_dic)
    num = list(map(lambda x:x+1, clothes_dic.values())) # value 값들 조합하기 위해 리스트 따로 생성
    return reduce(lambda x,y : x*y, num)-1 # num리스트에서 각자 곱하고 -1(아무것도 안 입은 상태)

