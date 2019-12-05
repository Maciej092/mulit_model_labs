from CA_gui import *
import sys


class MainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
