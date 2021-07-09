# A và B nhận được n cái túi, mỗi túi chứa từ 1 đến 2 viên kẹo. A và B phải tính toán sao cho khi chia xong n cái túi thì A và B đều nhận được lượng kẹo bằng nhau(không được lấy kẹo từ túi này chuyển sang túi khác). Hỏi A và B có thể nhận được số kẹo bằng nhau hay không.

# Ví dụ:

# Với bags = [1, 1, 1]. Đầu ra divideCandy(bags) = false.
#      Giải thích: Không có cách chia nào thỏa mãn.

# Với bags = [1, 2, 1, 2]. Đầu ra divideCandy(bags) = true.
#      Giải thích: A lấy túi 1, 3; B lấy túi 2, 4

# Đầu vào/Đầu ra

# [Giới hạn thời gian chạy] 0.5s với C++, 3s với Java và C#, 4s với Python, JS và Go

# [Đầu vào]array of integers
# 1 <= bags.length <= 10^4.
# bags[i] in [1, 2]
# [Đầu ra] boolean
#       Có thể chia số túi để A và B có số lượng kẹo bằng nhau hay không
def divideCandy(bags):
    bags.sort()
    sum1 = 0
    sum2 = 0
    for i in bags:
        sum2 += i
    if sum2 % 2 == 1:
        return False
    ans = sum2 // 2
    for i in range (0, len(bags) - 1):
        if (sum1 + bags[i] < ans): 
            sum1 += bags[i]
        else:
            if (sum1 + bags[i] == ans):
                return True
            else:
                if (bags[0] == 1):
                    return True
                else:
                    return False

    return False
arr=[1, 1, 1]
print(divideCandy(arr))#false
#dsdsasgikk