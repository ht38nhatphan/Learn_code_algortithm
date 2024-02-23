

# #liệt kê danh sách
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
# steps_list = solution_instance.climbStairs(5)
# print("List of steps:", steps_list)


#không liệt kê danh sách

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        # Initialize an array to store the number of ways to reach each step
        dp = [0] * (n + 1)

        # Base cases
        dp[1] = 1
        dp[2] = 2
        
        # Fill the dp array by iterating from step 3 to n
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            print(dp)

        return dp[n]

# Example usage:
solution_instance = Solution()
result = solution_instance.climbStairs(3)
print(result)
