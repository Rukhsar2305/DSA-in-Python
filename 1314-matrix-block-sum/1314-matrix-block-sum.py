class Solution(object):
    def matrixBlockSum(self, mat, k):
        
        m = len(mat)
        n = len(mat[0])

        #Create prefix sum matrix
        prefix = [[0] * (n+1) for _ in range(m+1)]

        #Build 2D prefix sum
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = (
                    mat[i][j]
                    + prefix[i][j+1]
                    + prefix[i+1][j]
                    - prefix[i][j]
                )

        #Calculate block sum
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                r1 = max(0, i - k)
                c1 = max(0, j -k)

                r2 = min(m, i + k + 1)
                c2 = min(n, j + k + 1)

                result[i][j] = (
                    prefix[r2][c2]
                    - prefix[r1][c2]
                    - prefix[r2][c1]
                    + prefix[r1][c1]
                )
        
        return result