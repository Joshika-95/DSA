matrix=[
    [1,1,1],
    [1,0,1],
    [1,1,0]
]
rows=len(matrix)
col=len(matrix[0])
zero_rows=[]
zero_col=[]
for i in range(rows):
    for j in range(col):
        if(matrix[i][j]==0):
            zero_rows.append(i)
            zero_col.append(j)
for i in zero_rows:
    for j in range(col):
        matrix[i][j]=0
for j in zero_col:
    for i in range(rows):
        matrix[i][j]=0
for row in matrix:
    print(row)