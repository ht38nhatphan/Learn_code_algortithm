class Solution(object):
    def multiply(self, num1, num2):
        if(num1 == None and num2 == None):
            return None
        #khởi tạo độ dài của 2 mảng
        m = len(num1)
        n = len(num2)

        if(m==0 or n==0 or num1 == '0' or num2 == '0'):
            return "0"
        if(num1=='1'):
            return num2
        if(num2 == '1'):
            return num1
        
        # Kết quả có thể có độ dài tối đa là m + n
        # vd 99*99 = 9801 (kết quả có độ dài 4)

        result = result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                
                # Tính giá trị của tích hai chữ số tại vị trí i và j.
                product += result[i + j + 1]

                # Cộng giá trị đã tính vào giá trị tại vị trí i + j + 1 của mảng kết quả.
                result[i + j + 1] = product % 10
                # Lưu chữ số hàng đơn vị vào vị trí i + j + 1 và cộng phần dư (chữ số hàng chục) vào vị trí i + j.
                result[i + j] += product // 10
        result_str = ""
        for r in result:
            # Bỏ qua số 0 đứng đầu
            if not result_str and r == 0:
                continue
            result_str += str(r)

        return result_str if result_str else "0"

        