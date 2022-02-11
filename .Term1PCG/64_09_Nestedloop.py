def convolute(M, K):
    # MatrixM = [[M[i][j] for j in range(len(M[0]))] for i in range(len(M))]
    # MatrixK = [[K[i][j] for j in range(len(K[0]))] for i in range(len(K))]
    # print(MatrixM, MatrixK)
    print((([M[i][j]+K[i][j] for j in range(len(K[0])) for i in range(len(K))])))

print(convolute([[1,2],[3,4]],[[1,1],[1,1]]))
print(convolute([[1,2,3],[4,5,6],[7,8,9]],[[-1,-2,-1],[0,0,0],[1,2,1]])) 
# exec(input().strip())