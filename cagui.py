import pyqtgraph as pg
import numpy as np
from PyQt5 import QtCore, QtWidgets
from pyqtgraph import ImageView
from ca_algorithm import CellularAutomata


class Ui_MainWindow(object):
    def __init__(self):
        self._timer = QtCore.QTimer()
        self._number_of_clicked = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 876)
        pg.setConfigOption('background', 'w')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.comboBox_neighbourRule = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_neighbourRule.setObjectName("comboBox_2")
        self.comboBox_neighbourRule.addItem("")
        self.comboBox_neighbourRule.addItem("")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_neighbourRule)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.comboBox_borderRule = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_borderRule.setObjectName("comboBox")
        self.comboBox_borderRule.addItem("")
        self.comboBox_borderRule.addItem("")


        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_borderRule)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.lineEdit_spaceSize = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_spaceSize.setObjectName("lineEdit")

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_spaceSize)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.lineEdit_randomGrain = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_randomGrain.setObjectName("lineEdit_2")

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_randomGrain)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButton_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.pushButton_5)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.radioButton)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        # Animation and displaying widget
        self.graphicsView = ImageView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 500))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.ui.histogram.hide()
        self.graphicsView.ui.roiBtn.hide()
        self.graphicsView.ui.menuBtn.hide()
        self.graphicsView.show()

        self.verticalLayout.addWidget(self.graphicsView)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButton_init = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_init.setObjectName("pushButton_init")
        self.pushButton_init.clicked.connect(self.init_ca_algo)
        self.verticalLayout_2.addWidget(self.pushButton_init)
        # Push button START/STOP
        self.pushButton_startStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_startStop.setObjectName("pushButton_3")
        self.pushButton_startStop.clicked.connect(self._init_image_timer)
        self.verticalLayout_2.addWidget(self.pushButton_startStop)

        self.pushButton_oneStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_oneStep.setObjectName("pushButton")
        self.pushButton_oneStep.clicked.connect(self._one_step)
        self.verticalLayout_2.addWidget(self.pushButton_oneStep)

        self.pushButton_clearSpace = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearSpace.setObjectName("pushButton_2")
        self.pushButton_clearSpace.clicked.connect(self._clear_space)

        self.verticalLayout_2.addWidget(self.pushButton_clearSpace)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Neighbours rule"))
        self.comboBox_neighbourRule.setItemText(0, _translate("MainWindow", "VONNEUMANN"))
        self.comboBox_neighbourRule.setItemText(1, _translate("MainWindow", "MOORE"))
        self.label_3.setText(_translate("MainWindow", "Border rule"))
        self.comboBox_borderRule.setItemText(0, _translate("MainWindow", "ABSORBING"))
        self.comboBox_borderRule.setItemText(1, _translate("MainWindow", "SNAKELIKE"))
        self.label_2.setText(_translate("MainWindow", "Space size"))
        self.lineEdit_spaceSize.setText(_translate("MainWindow", "50"))
        self.label_4.setText(_translate("MainWindow", "Number of grains"))
        self.lineEdit_randomGrain.setText(_translate("MainWindow", "10"))
        self.pushButton_4.setText(_translate("MainWindow", "Import csv"))
        self.pushButton_5.setText(_translate("MainWindow", "Export csv"))
        self.radioButton.setText(_translate("MainWindow", "Extended mode"))
        self.pushButton_startStop.setText(_translate("MainWindow", "Start/Stop"))
        self.pushButton_oneStep.setText(_translate("MainWindow", "Step"))
        self.pushButton_clearSpace.setText(_translate("MainWindow", "Clear space"))
        self.pushButton_init.setText(_translate("MainWindow", "Init space"))

    def init_ca_algo(self):
        self._ca_algo = CellularAutomata(int(self.lineEdit_randomGrain.text()),
                                         int(self.lineEdit_spaceSize.text()),
                                         int(self.lineEdit_spaceSize.text()),
                                         str(self.comboBox_borderRule.currentText()),
                                         str(self.comboBox_neighbourRule.currentText()))
        self._ca_algo.add_random()
        self.generatePgColormap()
        self.graphicsView.setImage(self._ca_algo.space)

    def _init_image_timer(self):
        self._number_of_clicked += 1
        if self._number_of_clicked % 2:
            self._timer.timeout.connect(self._update_func)
            self._timer.start(50)
        else:
            self._timer.stop()

    def _update_func(self):
        if self._ca_algo.cell_empty in self._ca_algo.space:
            self._ca_algo.one_step()
        self.graphicsView.setImage(self._ca_algo.space)

    def _clear_space(self):
        self._timer.stop()
        self._ca_algo.space = self._ca_algo.space_clear
        self.graphicsView.clear()

    def _one_step(self):
        self._timer.stop()
        self._ca_algo.one_step()
        self.graphicsView.setImage(self._ca_algo.space)

    def generatePgColormap(self):
        self.pos = np.linspace(0.0, 1.0, 2 + int(self.lineEdit_randomGrain.text()))
        self.cmap = pg.ColorMap(pos=self.pos, color=self._ca_algo.color_id)
        self.graphicsView.setColorMap(self.cmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
