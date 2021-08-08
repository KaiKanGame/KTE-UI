from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KTE(object):
    def setupUi(self, KTE):
        KTE.setObjectName("KTE")
        KTE.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(KTE)
        self.centralwidget.setObjectName("centralwidget")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(220, 10, 91, 33))
        self.save.setObjectName("save")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(320, 10, 91, 33))
        self.open.setObjectName("open")
        self.new_2 = QtWidgets.QPushButton(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(420, 10, 91, 33))
        self.new_2.setObjectName("new_2")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 191, 541))
        self.treeView.setObjectName("treeView")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(220, 90, 561, 461))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setText("test")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 62, 561, 21))
        self.lineEdit.setObjectName("lineEdit")
        KTE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KTE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        KTE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KTE)
        self.statusbar.setObjectName("statusbar")
        KTE.setStatusBar(self.statusbar)

        self.retranslateUi(KTE)
        QtCore.QMetaObject.connectSlotsByName(KTE)

    def retranslateUi(self, KTE):
        _translate = QtCore.QCoreApplication.translate
        KTE.setWindowTitle(_translate("KTE", "MainWindow"))
        self.save.setText(_translate("KTE", "Save"))
        self.open.setText(_translate("KTE", "open"))
        self.new_2.setText(_translate("KTE", "new"))
        self.lineEdit.setText(_translate("KTE", "filename:"))

