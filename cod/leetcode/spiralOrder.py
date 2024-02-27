
class Solution(object):
    def spiralOrder(self, matrix):
        m,n = len(matrix),len(matrix[0])
        results,arr = self.outline(matrix, m,n)
        i = len(arr)
        results_arr = []
        results_arr += results
        while i>0:
            results,arr = self.outline(arr, i,len(arr[0]))
            results_arr += results
            i = len(arr)
        return results_arr

    def outline(self,matrix,m,n):
        # Duyệt qua vòng ngoài của ma trận và hiển thị giá trị
        outer_ring_values,arr1,arr2,arrnew = [],[],[],[]
        matrixnew = []
        for i in range(m):
            check = False
            for j in range(n):
                if i == 0 or j == n - 1:
                    outer_ring_values.append(matrix[i][j])
                    check = True
                if j == 0 and check == False:
                    arr1.append(matrix[i][j])
                    check = True
                if i == m-1 and check == False:
                    arr2.append(matrix[i][j])
                    check = True
                if check == False: 
                    arrnew.append(matrix[i][j])
                check = False
            if(len(arrnew)!=0):
                matrixnew.append(arrnew)
                arrnew = []
        fullarr = outer_ring_values + arr2[::-1] +arr1[::-1]
        return fullarr,matrixnew
        