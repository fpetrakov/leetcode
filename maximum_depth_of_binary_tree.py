class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthStack(self, root: TreeNode | None) -> int:
        stack = [[root, 0]]
        res = 0

        while stack:
            node, depth = stack.pop()
            res = max(res, depth)

            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res
