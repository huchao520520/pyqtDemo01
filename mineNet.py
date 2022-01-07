import random

class mineNet:
    length = 10
    width = 10
    mineNumber = 10
    mineCoordinate = []
    mineNet = [[]]

    def __init__(self, length, width, mineNumber):
        self.length = length
        self.width = width
        self.mineNumber = mineNumber
        self.generateMineNet(length, width, mineNumber)

    def generateMineNet(self, length, width, mineNum):
        """
        生成雷网
        :param length: 长度
        :param width: 宽度
        :param mineNum: 雷数量
        :return: 雷网二维数组
        """
        while len(self.mineCoordinate) < mineNum:
            randomLen = random.randint(1, length)
            randomWid = random.randint(1, width)
            self.mineCoordinate.append({randomLen: randomWid})
        print('雷的坐标:')
        print(self.mineCoordinate)
        self.mineNet = [[0 for col in range(width)] for row in range(length)]
        for l in range(length):
            for w in range(width):
                ele = {l + 1: w + 1}
                self.mineNet[l][w] = 1 if ele in self.mineCoordinate else 0
        print('雷网:')
        print(self.mineNet)

    def gridClick(self, ):
        print('a')