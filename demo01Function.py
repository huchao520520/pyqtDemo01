import random

def prints():
    print('a')

def generateMineNet(length, width, mineNum):
    """
    生成雷网
    :param length: 长度
    :param width: 宽度
    :param mineNum: 雷数量
    :return: 雷网二维数组
    """
    mineNet = [[0 for col in range(width)] for row in range(length)]
    mineCoordinate = []
    while len(mineCoordinate) < mineNum:
        randomLen = random.randint(1, length)
        randomWid = random.randint(1, width)
        mineCoordinate.append({randomLen: randomWid})
    print('雷的坐标:')
    print(mineCoordinate)
    for l in range(length):
        for w in range(width):
            ele = {l + 1: w + 1}
            mineNet[l][w] = 1 if ele in mineCoordinate else 0
    print('雷网:')
    print(mineNet)
    return mineNet
