# 从简单的1个扇形对应m个颜色开始推导，2个 3个由此得到递推公式


def count(n, m):
    e_ = 1e9 + 7
    if n == 1:
        return m % e_
    if n == 2:
        return (m * m - 1) % e_

    result = [0] * n
    result[0] = m % e_
    result[1] = (m * (m - 1)) % e_
    result[2] = (m * (m - 1)*(m-2)) % e_

    for i in range(3, n):
        result[i] = (result[i - 1] * (m - 2) + result[i - 2] * (m - 1)) % (e_)

    return int(result[n - 1])


print(count(4, 6))
