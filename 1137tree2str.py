class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree2str(t):
    result = solution(t)
    return result[1:len(result)-1]


def solution(t):
    if t is None:
        return "()"

    if t.left is None and t.right is None:
        return "(" + t.val + ")"

    left = solution(t.left)
    right = solution(t.right)

    return "(" + t.val + left + "" if right == "()" else right + ")"
