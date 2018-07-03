# -*- coding: utf-8 -*-


class Totems(object):
    def __init__(self):
        self.list_2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        # list_2为最终目标

    def pass01(self, n):
        # 开关灯转换
        if n == 0:
            n = 1
        else:
            n = 0
        return n

    def totems_pass(self, i, j, m):
        # 每次开关灯影响周围4格
        m[i][j] = self.pass01(m[i][j])
        if i >= 1:
            m[i-1][j] = self.pass01(m[i-1][j])
            # 左
        if i < 4:
            m[i+1][j] = self.pass01(m[i+1][j])
            # 右
        if j >= 1:
            m[i][j-1] = self.pass01(m[i][j-1])
            # 上
        if j < 4:
            m[i][j+1] = self.pass01(m[i][j+1])
            # 下
        return m

    def pass_totems(self, m):
        # 判断是否满足需求
        if m == self.list_2:
            return True
        else:
            return None

    def main(self):
        for n in range(0, 33554432):
            # 转换为二进制
            n = '{:025b}'.format(n)
            # list_1为初始状态
            list_1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            for m in range(0, 25):
                if n[m] == '0':
                    z = m / 5
                    x = m % 5
                    list_1 = self.totems_pass(z, x, list_1)
                    if self.pass_totems(list_1) is True:
                        return n

if __name__ == '__main__':
    a = Totems()
    c = a.main()
    print c
