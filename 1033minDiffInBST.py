import sys
def minDiffInBST(root):
# Write your code here
    nodeList = []

    inOrder(root, nodeList)

    k = sys.maxsize
    for i in range(1, len(nodeList)):
        k = min(k, nodeList[i]-nodeList[i-1])

    return k


def inOrder(root, nodeList):
    if root is None:
        return

    inOrder(root.left, nodeList)
    nodeList.append(root.val)
    inOrder(root.right, nodeList)