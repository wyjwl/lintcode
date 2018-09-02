class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(root):
        if not root:
            return 0
        sum = 0
        if root.left:
            left = root.left
            if not left.left and not left.right:
                sum += left.val
            else:
                sum += dfs(left)
        if root.right:
            right = root.right
            sum += dfs(right)
        return sum

    return dfs(root)
