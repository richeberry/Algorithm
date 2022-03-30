# Programmers _ Lv.2 헹렬 테두리 회전하기


def solution(rows, columns, queries):
    answer = []
    mat_list = [i for i in range(1,(rows*columns)+1)] # 1부터 rows*columns 까지 리스트 만든 후 
    mat = [mat_list[i:i+columns] for i in range(0,len(mat_list), columns)]
    
    for query in queries:
        query = [x-1 for x in query] # 인덱스이므로 -1
        tmp = mat[query[0]][query[1]] # 왼쪽 위 값 = 시작값
        small = tmp
        
        # 왼쪽 위 값부터 오른쪽 위 값까지
        for i in range(query[0]+1, query[2]+1):
            mat[i-1][query[1]] = mat[i][query[1]]
            small = min(small, mat[i][query[1]])
            
        # 왼쪽 아래 값부터 오른쪽 아래 값까지
        for i in range(query[1]+1, query[3]+1):
            mat[query[2]][i-1] = mat[query[2]][i]
            small = min(small, mat[query[2]][i])
            
        # 왼쪽 위 값부터 왼쪽 아래 값까지
        for i in range(query[2]-1, query[0]-1, -1):
            mat[i+1][query[3]] = mat[i][query[3]]
            small = min(small, mat[i][query[3]])
            
        # 오른쪽 위 값부터 오른쪽 아래 값까지
        for i in range(query[3]-1, query[1]-1, -1):
            mat[query[0]][i+1] = mat[query[0]][i]
            small = min(small, mat[query[0]][i])
        mat[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer
