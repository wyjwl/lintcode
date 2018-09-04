def searchRange(root, k1, k2):
    if root is None:
        return []
    result = []
    traversal(root, k1, k2, result)
    return result


def traversal(root, k1, k2, result):

    if root is None:
        return

    traversal(root.left, k1, k2, result)
    if root.val >= k1 and root.val <= k2:
        result.append(root.val)
    traversal(root.right, k1, k2, result)