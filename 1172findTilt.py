class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def findTilt(root):
    if root is None:
        return 0
    count = [0]

    traverse(root, count)

    return count[0]


def traverse(root, count):
    if root is None:
        return 0

    left = traverse(root.left, count)
    right = traverse(root.right, count)

    count[0] += abs(left - right)

    return root.val + left + right
