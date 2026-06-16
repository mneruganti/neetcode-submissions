# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            # left and right contain recursive calls so left[0] gets whether the node's left is None or not
            # left[1] and right[1] get the height of the tree from the dfs call
            balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0] # we only want the bool