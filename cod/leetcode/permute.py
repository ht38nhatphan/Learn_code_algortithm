class TreeNode:
    def __init__(self, value, remain):
        self.value = value
        self.remain = remain
        self.children = []

class Solution(object):
    def generate_tree(self,tree_node, current, result):
        if not tree_node.remain:
            # Nếu không còn phần tử nào còn lại, thêm mảng vào kết quả
            result.append(list(current))
            return

        for i, num in enumerate(tree_node.remain):
            # Tạo nút con mới với giá trị là số hiện tại và các số còn lại
            child_node = TreeNode(num, tree_node.remain[:i] + tree_node.remain[i+1:])
            tree_node.children.append(child_node)

            # Đệ quy để xử lý mức tiếp theo
            self.generate_tree(child_node, current + [num], result)
    def permute(self, nums):
        root = TreeNode(None, nums)
        result = []
        self.generate_tree(root, [], result)
        return result
# Test với nums = [1, 2, 3]
nums = [1]
sl = Solution()
a = sl.permute(nums)
# permutations = generate_permutations_wrapper(nums)
print(a)