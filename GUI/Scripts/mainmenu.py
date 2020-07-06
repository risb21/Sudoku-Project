# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import SudokuGridlayout
from random import choice, randint
import SudokuClass

class MainmenuUI(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 532)
        MainWindow.setFixedSize(448, 532)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainMenu_background_label = QtWidgets.QLabel(self.centralwidget)
        self.mainMenu_background_label.setGeometry(QtCore.QRect(-10, 0, 461, 521))
        self.mainMenu_background_label.setText("")
        self.mainMenu_background_label.setPixmap(QtGui.QPixmap(r".\GUI\Resources\bgtest-3.png"))
        self.mainMenu_background_label.setScaledContents(True)
        self.mainMenu_background_label.setObjectName("mainMenu_background_label")

        self.mainMenu_heading = QtWidgets.QLabel(self.centralwidget)
        self.mainMenu_heading.setGeometry(QtCore.QRect(80, 90, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(36)
        self.mainMenu_heading.setFont(font)
        self.mainMenu_heading.setObjectName("mainMenu_heading")

        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(160, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(18)
        self.play_button.setFont(font)
        self.play_button.setStyleSheet("QPushButton{background: transparent;}QPushButton::hover\n"
"{\n"
"border : 3px solid black;\n"
"}")
        self.play_button.setObjectName("play_button")
        self.play_button.clicked.connect(self.play_button_clicked)

        self.top_score_button = QtWidgets.QPushButton(self.centralwidget)
        self.top_score_button.setEnabled(False)
        self.top_score_button.setGeometry(QtCore.QRect(160, 272, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(16)
        self.top_score_button.setFont(font)
        self.top_score_button.setStyleSheet("QPushButton{background: transparent;}")
        self.top_score_button.setObjectName("top_score_button")

        self.more_options_button = QtWidgets.QPushButton(self.centralwidget)
        self.more_options_button.setEnabled(False)
        self.more_options_button.setGeometry(QtCore.QRect(160, 330, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(16)
        self.more_options_button.setFont(font)
        self.more_options_button.setStyleSheet("QPushButton{background: transparent;}")
        self.more_options_button.setObjectName("more_options_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku!"))
        self.mainMenu_heading.setText(_translate("MainWindow", "SUDOKU"))
        self.play_button.setText(_translate("MainWindow", "PLAY"))
        self.top_score_button.setText(_translate("MainWindow", "TOP"))
        self.more_options_button.setText(_translate("MainWindow", "MORE.."))

    def play_button_clicked(self):
        self.MainWindow.hide()
        sudoku_screen.show()

    def topscore_clicked(self):
        pass

    def more_clicked(self):
        pass
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainmenu_mainwindow = QtWidgets.QMainWindow()
    mainmenu_ui = MainmenuUI()
    mainmenu_ui.setupUi(mainmenu_mainwindow)
    mainmenu_mainwindow.show()

    global sudoku_screen
    sudoku_screen = QtWidgets.QMainWindow()
    test_sudoku_obj = SudokuClass.Sudoku()
    for i in test_sudoku_obj:
        for j in i:
            j.set_value(choice([randint(1,9),None]))

    BOARD = []
    for i in test_sudoku_obj.get_all_rows():
        BOARD.append(list(map(SudokuClass._Element.get_value, i)))

    sudoku_ui = SudokuGridlayout.SudokuMainWindow(BOARD)
    sudoku_ui.setupUi(sudoku_screen)
    
    sys.exit(app.exec_())