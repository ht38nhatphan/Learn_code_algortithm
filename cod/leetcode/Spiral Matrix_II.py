class Solution(object):

    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        value = 1
        vt1,vt2= 0,n
        while(value<= n * n):
            
            temp= vt1
            # duyệt trái qua phải 
            for row in range(len(matrix[vt1])):
                if(matrix[vt1][row]==0): 
                    matrix[vt1][row] = value
                    value += 1

            #duyệt trên xuống dưới
            for col in range(vt1+1,vt2):
                if(matrix[col][vt2-1] ==0):
                    matrix[col][vt2-1] = value
                    value += 1
            #duyệt phải qua trái
            j = vt2-2
            while j>=0:
                if(matrix[vt2-1][j] ==0):
                    matrix[vt2-1][j] = value
                    value +=1
                j -=1
            

            #duyệt dưới lên trên
            up = vt2-2
            while up>=1:
                if(matrix[up][vt1] ==0):
                    matrix[up][vt1] = value
                    value +=1
                up -= 1

            vt1,vt2 = vt1+1,vt2-1
        return matrix

sl = Solution()
result = sl.generateMatrix(4)
print(result)