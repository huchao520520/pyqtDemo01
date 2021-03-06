# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo01.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mineNet
import demo01Function


class Ui_Dialog(object):
    """
    扫雷窗口
    """

    def setupUi(self, Dialog):
        length = 10
        width = 10
        mineNumber = 10
        gridSize = 20
        totalLength = length * gridSize
        totalWidth = width * gridSize
        net = mineNet.mineNet(length, width, mineNumber)
        mine_net = net.mineNet
        for rowNo in range(len(mine_net)):
            for columnNo in range(len(mine_net[rowNo])):
                self.toolButton = QtWidgets.QToolButton(Dialog)
                self.toolButton.setGeometry(QtCore.QRect(gridSize * rowNo, gridSize * columnNo, gridSize, gridSize))
                self.toolButton.setObjectName("toolButton")
                self.toolButton.clicked.connect(lambda: net.gridClick({rowNo: columnNo}))

        Dialog.setObjectName("Dialog")
        Dialog.resize(totalLength, totalWidth)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Mine", "Mine"))
        self.toolButton.setText(_translate("Mine", " "))
