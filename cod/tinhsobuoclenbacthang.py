class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Nếu n không hợp lệ, trả về danh sách trống
        if n <= 0:
            return []

        # Khởi tạo một danh sách 2 chiều để lưu các cách leo lên cầu thang
        ways = [[] for _ in range(n + 1)]
        # Khởi tạo một danh sách con trống cho trường hợp ban đầu (0 bước)
        ways[0] = [[]]

        # Lặp qua số bước từ 1 đến n
        for i in range(1, n + 1):
            # Lặp qua các bước có thể là 1 hoặc 2
            for step in [1, 2]:
                # Kiểm tra xem có thể thêm bước này không
                if i - step >= 0:
                    # Thêm mỗi cách từ bước trước đó vào danh sách
                    for prev_way in ways[i - step]:
                        ways[i].append(prev_way + [step])

        # Trả về danh sách các cách leo lên cầu thang với n bước
        return ways[n]

# Ví dụ sử dụng:
solution_instance = Solution()
steps_list = solution_instance.climbStairs(3)
print("List of steps:", steps_list)


##Cach2
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         def generate_steps(current, remaining):
#             if remaining == 0:
#                 return [current[:]]

#             ways = []
#             if remaining >= 1:
#                 current.append(1)
#                 ways += generate_steps(current, remaining - 1)
#                 current.pop()

#             if remaining >= 2:
#                 current.append(2)
#                 ways += generate_steps(current, remaining - 2)
#                 current.pop()

#             return ways

#         return generate_steps([], n)

# # Example usage:
# solution_instance = Solution()
# steps_list = solution_instance.climbStairs(3)
# print("List of steps:", steps_list)
