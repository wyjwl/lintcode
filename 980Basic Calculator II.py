def calculate(s):
    if s is None or len(s) == 0:
        return 0

    tools = list()
    sign = '+'
    num = 0
    for i in range(0, len(s)):

        c = s[i]

        if str.isnumeric(c):
            num = 10 * num + int(c)

        if c != ' ' and not str.isnumeric(c) or i + 1 == len(s):
            if sign == '+':
                tools.append(num)
            elif sign == '-':
                tools.append(-num)
            elif sign == '*':
                tools.append(tools.pop() * num)
            elif sign == '/':
                tools.append(int(tools.pop() / num))

            sign = c
            num = 0

    res = 0
    while not len(tools) == 0:
        res += tools.pop()

    return res
