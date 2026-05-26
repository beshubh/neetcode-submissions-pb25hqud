class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        output = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    output[i][j] += mat1[i][k] * mat2[k][j]
        return output



 