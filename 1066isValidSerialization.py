#1. 数字的个数总是比#号少一个

#2. 最后一个一定是#号

#那么我们加入先不考虑最后一个#号，那么此时数字和#号的个数应该相同，
# 如果我们初始化一个为0的计数器，遇到数字，计数器加1，遇到#号，计数器减1，那么到最后计数器应该还是0。
# 下面我们再来看两个返回False的例子，"#,7,6,9,#,#,#"和"7,2,#,2,#,#,#,6,#"，
# 那么通过这两个反例我们可以看出，如果根节点为空的话，后面不能再有节点，
# 而且不能有三个连续的#号出现。所以我们再加减计数器的时候，如果遇到#号，
# 且此时计数器已经为0了，再减就成负数了，就直接返回False了，因为正确的序列里，
# 任何一个位置i，在[0, i]范围内的#号数都不大于数字的个数的。当循环完成后，
# 我们检测计数器是否为0的同时还要看看最后一个字符是不是#号


def isValidSerialization(preorder):
    splitStr = preorder.split(",")
    count = 0
    for i in range(0, len(splitStr)-1):
        if splitStr[i].isnumeric():
            count += 1

        if splitStr[i] == "#":
            count -= 1

        if count < 0:
            return False

    return splitStr[len(splitStr)-1] == "#"
