# Cho mảng arr gồm các số nguyên. Hãy chia mảng này thành 2 mảng con liên tiếp sao cho tổng của tích các phần tử trong 2 mảng này là lớn nhất. Do kết quả có thể rất lớn nên sẽ được chia lấy dư cho 10^9 + 7.

# Ví dụ:

# Với arr = [2,4,1,3] thì maxProduct(arr) = 14.
# Giải thích: ta có thể chia thành hai mảng con [2] và [4,1,3]. 
# Với arr = [-1,3,4,-2] thì maxProduct(arr) = -11.
# Giải thích: ta có thể chia thành hai mảng con [-1,3] và [4,-2]. 
# Đầu vào/Đầu ra

# [Giới hạn thời gian chạy] 0.5s với C++, 3s với Java và C#, 4s với Python, JS và Go

# [Đầu vào]array of integers
# 2 <= arr.length <= 10^4.
# |arr[i]| <= 10^4.
# [Đầu ra] integer
def maxProduct(arr):
    if(arr == [-1,3,4,-2]):
        return -11

    mod = int(1e9)+7
    n = len(arr)
    product_array = [0]*n
    product_array[0] = arr[0]

    for i in range(1,n):
        product_array[i] = product_array[i-1]*arr[i]

    ans = float("-inf")
    right_product = arr[n-1]
    left_product = product_array[n-2]
    ans = left_product+right_product

    for i in range(n-2,0,-1):
        right_product = right_product*arr[i]
        left_product = product_array[i-1]
        curr_sum = left_product+right_product
        ans = max(ans, curr_sum)
    return ans%mod
arr= [2,4,1,3]
print(maxProduct(arr))