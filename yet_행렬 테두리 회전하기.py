# 행렬 테두리 회전하기

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

mat = [i for i in range(1,(rows*columns)+1)] # 1부터 rows*columns 까지 리스트 만든 후 
mat = [mat[i:i+columns] for i in range(0,len(mat), columns)] # 행렬으로 만들기

# print(mat)

for q in queries:
    q = [q[i:i+2] for i in range(0, len(q), 2)]
    # print(q)
    save = q 
    # 매트릭스 한 칸씩 이동
    for ix in q:
        print(ix)


    # start = mat[q[0][0]-1][q[0][1]-1]
    # last = mat[q[1][0]-1][q[1][1]-1]
    # print(start, last)
    