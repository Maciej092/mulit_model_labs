import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pyqtgraph import ImageView
from pyqtgraph import setConfigOption, ColorMap
from ca_algorithm import CellularAutomata
from ca_algorithm_gbc import CellularAutomataGBC
from multiprocessing import Pool


class Ui_MainWindow(object):
    def __init__(self):
        self.timer = QtCore.QTimer()
        self.gbc_is_on = False
        self.number_of_clicked = 0
        self.number_of_clicked_gbc = 0
        self.worker = Pool(1)
        self.result_space = None
        self.deleted_ids = list()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        setConfigOption('background', 'w')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.formLayout_settings = QtWidgets.QFormLayout()
        self.formLayout_settings.setObjectName("formLayout_settings")

        self.label_neighbours_rule = QtWidgets.QLabel(self.centralwidget)
        self.label_neighbours_rule.setObjectName("label_neighbours_rule")
        self.formLayout_settings.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_neighbours_rule)

        self.comboBox_neighbours_rule = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_neighbours_rule.setObjectName("comboBox_neighbours_rule")
        self.comboBox_neighbours_rule.addItem("")
        self.comboBox_neighbours_rule.addItem("")
        self.comboBox_neighbours_rule.addItem("")
        self.comboBox_neighbours_rule.addItem("")
        self.comboBox_neighbours_rule.addItem("")
        self.comboBox_neighbours_rule.addItem("")
        self.formLayout_settings.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_neighbours_rule)

        self.label_border_condition = QtWidgets.QLabel(self.centralwidget)
        self.label_border_condition.setObjectName("label_border_condition")
        self.formLayout_settings.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_border_condition)

        self.comboBox_border_condition = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_border_condition.setObjectName("comboBox_border_condition")
        self.comboBox_border_condition.addItem("")
        self.comboBox_border_condition.addItem("")
        self.formLayout_settings.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_border_condition)

        self.label_size_of_space = QtWidgets.QLabel(self.centralwidget)
        self.label_size_of_space.setObjectName("label_size_of_space")
        self.formLayout_settings.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_size_of_space)

        self.lineEdit_size_of_space = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_size_of_space.setObjectName("lineEdit_size_of_space")
        self.formLayout_settings.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_size_of_space)

        self.label_number_of_grains = QtWidgets.QLabel(self.centralwidget)
        self.label_number_of_grains.setObjectName("label_number_of_grains")
        self.formLayout_settings.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_number_of_grains)

        self.lineEdit_number_of_grains = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_of_grains.setObjectName("lineEdit_number_of_grains")
        self.formLayout_settings.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_number_of_grains)

        self.label_inclusions_number = QtWidgets.QLabel(self.centralwidget)
        self.label_inclusions_number.setObjectName("label_inclusions_number")
        self.formLayout_settings.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_inclusions_number)

        self.lineEdit_inclusions_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inclusions_number.setObjectName("lineEdit_inclusions_number")
        self.formLayout_settings.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inclusions_number)

        self.label_min_radius = QtWidgets.QLabel(self.centralwidget)
        self.label_min_radius.setObjectName("label_min_radius")
        self.formLayout_settings.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_min_radius)

        self.lineEdit_min_radius = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_min_radius.setObjectName("lineEdit_min_radius")
        self.formLayout_settings.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_min_radius)

        self.label_max_radius = QtWidgets.QLabel(self.centralwidget)
        self.label_max_radius.setObjectName("label_max_radius")
        self.formLayout_settings.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_max_radius)

        self.lineEdit_max_radius = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_max_radius.setObjectName("lineEdit_max_radius")
        self.formLayout_settings.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_max_radius)

        self.pushButton_gbc_feature = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gbc_feature.setObjectName("radioButton_gbc_feature")
        self.pushButton_gbc_feature.setStyleSheet("background-color: red")
        self.pushButton_gbc_feature.clicked.connect(self.controller_gbc_init)
        self.formLayout_settings.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushButton_gbc_feature)

        self.pushButton_delete_grains = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_grains.setObjectName("pushButton_delete_grains")
        self.pushButton_delete_grains.clicked.connect(self.view_delete_grains)
        self.formLayout_settings.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.pushButton_delete_grains)

        self.pushButton_keep_selected = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keep_selected.setObjectName("pushButton_keep_selected")
        self.pushButton_keep_selected.clicked.connect(self.view_keep_selected)
        self.formLayout_settings.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.pushButton_keep_selected)

        self.comboBox_list_of_grains = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_list_of_grains.setObjectName("comboBox_list_of_grains")
        self.formLayout_settings.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.comboBox_list_of_grains)

        self.pushButton_import_from_csv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import_from_csv.setObjectName("pushButton_import_from_csv")
        self.pushButton_import_from_csv.clicked.connect(self.io_open_file_name_dialog)
        self.formLayout_settings.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.pushButton_import_from_csv)

        self.pushButton_export_to_csv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_to_csv.setObjectName("pushButton_export_to_csv")
        self.pushButton_export_to_csv.clicked.connect(self.io_open_save_dialog)
        self.formLayout_settings.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.pushButton_export_to_csv)

        self.pushButton_export_to_png = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_to_png.setObjectName("pushButton_export_to_png")
        self.pushButton_export_to_png.clicked.connect(self.io_open_save_dialog_image)
        self.formLayout_settings.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.pushButton_export_to_png)

        self.line_horizontal = QtWidgets.QFrame(self.centralwidget)
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal.setObjectName("line")
        self.formLayout_settings.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.line_horizontal)

        self.pushButton_init_space = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_init_space.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_init_space.setObjectName("pushButton_init_space")
        self.pushButton_init_space.clicked.connect(self.controller_init_ca_algo)
        self.formLayout_settings.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.pushButton_init_space)

        self.pushButton_start_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_stop.setObjectName("pushButton_start_stop")
        self.pushButton_start_stop.clicked.connect(self.controller_init_image_timer)
        self.formLayout_settings.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.pushButton_start_stop)

        self.pushButton_step = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_step.setObjectName("pushButton_step")
        self.pushButton_step.clicked.connect(self.controller_one_step)
        self.formLayout_settings.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.pushButton_step)

        self.pushButton_clear_space = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_space.setObjectName("pushButton_clear_space")
        self.pushButton_clear_space.clicked.connect(self.view_clear_space)
        self.formLayout_settings.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.pushButton_clear_space)

        self.pushButton_draw_boundaries = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_draw_boundaries.setObjectName("pushButton_draw_boundaries")
        self.pushButton_draw_boundaries.clicked.connect(self.view_draw_boundaries)
        self.formLayout_settings.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.pushButton_draw_boundaries)

        self.pushButton_dual_phase = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dual_phase.setObjectName("pushButton_dual_phase")
        self.pushButton_dual_phase.clicked.connect(self.controller_init_dual_phase)
        self.formLayout_settings.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.pushButton_dual_phase)

        self.pushButton_dual_phase_init = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dual_phase_init.setObjectName("pushButton_dual_phase")
        self.pushButton_dual_phase_init.clicked.connect(self.controller_dual_phase_init)
        self.formLayout_settings.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.pushButton_dual_phase_init)

        self.pushButton_substructures = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_substructures.setObjectName("pushButton_dual_phase")
        self.pushButton_substructures.clicked.connect(self.controller_init_substructures)
        self.formLayout_settings.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.pushButton_substructures)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout_settings.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label)

        self.label_probability = QtWidgets.QLabel(self.centralwidget)
        self.label_probability.setObjectName("label_probability")
        self.formLayout_settings.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_probability)

        self.lineEdit_prob_threshold = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prob_threshold.setObjectName("lineEdit_prob_threshold")
        self.formLayout_settings.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prob_threshold)

        self.horizontalLayout.addLayout(self.formLayout_settings)

        self.line_vertical = QtWidgets.QFrame(self.centralwidget)
        self.line_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_vertical)

        self.graphicsView = ImageView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(501, 501))
        self.graphicsView.setMaximumSize(QtCore.QSize(501, 501))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.ui.histogram.hide()
        self.graphicsView.ui.roiBtn.hide()
        self.graphicsView.ui.menuBtn.hide()
        self.graphicsView.show()
        self.horizontalLayout.addWidget(self.graphicsView)

        # Other stuff
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.controller_init_ca_algo()
        # self._clear_space()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_neighbours_rule.setText(_translate("MainWindow", "Neighbours rule"))
        self.comboBox_neighbours_rule.setItemText(0, _translate("MainWindow", "VONNEUMANN"))
        self.comboBox_neighbours_rule.setItemText(1, _translate("MainWindow", "MOORE"))
        self.comboBox_neighbours_rule.setItemText(2, _translate("MainWindow", "HEXAGONAL_LEFT"))
        self.comboBox_neighbours_rule.setItemText(3, _translate("MainWindow", "HEXAGONAL_RIGHT"))
        self.comboBox_neighbours_rule.setItemText(4, _translate("MainWindow", "PENTAGONAL_LEFT"))
        self.comboBox_neighbours_rule.setItemText(5, _translate("MainWindow", "PENTAGONAL_RIGHT"))
        self.label_border_condition.setText(_translate("MainWindow", "Border rule"))
        self.comboBox_border_condition.setItemText(0, _translate("MainWindow", "ABSORBING"))
        self.comboBox_border_condition.setItemText(1, _translate("MainWindow", "SNAKELIKE"))
        self.label_size_of_space.setText(_translate("MainWindow", "Size of space"))
        self.lineEdit_size_of_space.setText(_translate("MainWindow", "100"))
        self.label_number_of_grains.setText(_translate("MainWindow", "Number of grains"))
        self.lineEdit_number_of_grains.setText(_translate("MainWindow", "120"))
        self.label_inclusions_number.setText(_translate("MainWindow", "Number of incl."))
        self.lineEdit_inclusions_number.setText(_translate("MainWindow", "0"))
        self.label_min_radius.setText(_translate("MainWindow", "Min radius"))
        self.lineEdit_min_radius.setText(_translate("MainWindow", "1"))
        self.label_max_radius.setText(_translate("MainWindow", "Max radius"))
        self.lineEdit_max_radius.setText(_translate("MainWindow", "6"))
        self.pushButton_gbc_feature.setText(_translate("MainWindow", "GBC feature"))
        self.pushButton_delete_grains.setText(_translate("MainWindow", "Delete grains"))
        self.pushButton_keep_selected.setText(_translate("MainWindow", "Keep selected"))
        self.pushButton_import_from_csv.setText(_translate("MainWindow", "Import csv"))
        self.pushButton_export_to_csv.setText(_translate("MainWindow", "Export csv"))
        self.pushButton_export_to_png.setText(_translate("MainWindow", "Export png"))
        self.pushButton_init_space.setText(_translate("MainWindow", "Init space"))
        self.pushButton_start_stop.setText(_translate("MainWindow", "Start/Stop"))
        self.pushButton_step.setText(_translate("MainWindow", "Step"))
        self.pushButton_clear_space.setText(_translate("MainWindow", "Clear space"))
        self.pushButton_draw_boundaries.setText(_translate("MainWindow", "Draw bound."))
        self.pushButton_dual_phase.setText(_translate("MainWindow", "Dual phase"))
        self.pushButton_dual_phase_init.setText(_translate("MainWindow", "Dual init"))
        self.pushButton_substructures.setText(_translate("MainWindow", "Substructures"))
        self.label_probability.setText(_translate("MainWindow", "Probability"))
        self.lineEdit_prob_threshold.setText(_translate("MainWindow", "60"))

    def view_generate_pg_colormap(self):
        self.pos = np.linspace(0.0, 1.0, self._ca_algo.number_of_reserved_ids+int(self.lineEdit_number_of_grains.text()))
        self.cmap = ColorMap(pos=self.pos, color=self._ca_algo.color_id)
        self.graphicsView.setColorMap(self.cmap)

    def view_display_image(self):
        self.graphicsView.setImage(self._ca_algo.space.T, levels=(0.0, self._ca_algo.number_of_reserved_ids+float(self.lineEdit_number_of_grains.text())))

    def view_generate_set_of_ids(self):
        self.comboBox_list_of_grains.clear()
        for item in self._ca_algo.list_of_id:
            self.comboBox_list_of_grains.addItem(str(item))
        self.comboBox_list_of_grains.setEnabled(False)
        self.pushButton_delete_grains.setEnabled(False)
        self.pushButton_keep_selected.setEnabled(False)

    def view_delete_grains(self):
        id_to_delete = int(self.comboBox_list_of_grains.currentText())
        if id_to_delete in self._ca_algo.space:
            self._ca_algo.space[self._ca_algo.space == id_to_delete] = 0
            self.result_space = None
            self.deleted_ids.append(id_to_delete)
            self.view_display_image()
        else:
            return

    def view_keep_selected(self):
        id_to_keep = int(self.comboBox_list_of_grains.currentText())
        if id_to_keep in self._ca_algo.space:
            self._ca_algo.space[self._ca_algo.space != id_to_keep] = 0
            self.result_space = None

            self.view_display_image()
        else:
            return

    def view_draw_boundaries(self):
        for x in range(self._ca_algo.space_width):
            for y in range(self._ca_algo.space_width):
                c  = self._ca_algo.space[x, y]
                if x < self._ca_algo.space_width-1:
                    c1 = self._ca_algo.space[x+1, y]
                else:
                    c1 = c
                if y < self._ca_algo.space_width-1:
                    c2 = self._ca_algo.space[x, y+1]
                else:
                    c2 = c
                if c > 1 and (c != c1 or c != c2):
                    self._ca_algo.space[x, y] = 1
        self.result_space = self._ca_algo.space
        self.view_display_image()
        grain_boundaries = np.count_nonzero(self._ca_algo.space == 1)
        grain_size = len(self._ca_algo.list_of_id)
        grain_aver = (self._ca_algo.space_width * self._ca_algo.space_width) / grain_size
        msg = QMessageBox()
        msg.setWindowTitle('Result')
        msg.setText('Total length of the boundaries: ' + str(grain_boundaries) + '\n' +
                    'Average size of a grain: '        + str(int(grain_aver)))
        msg.exec_()

    def view_clear_space(self):
        self.result_space = None
        self.timer.stop()
        self._ca_algo.space = self._ca_algo.space_clear
        self.graphicsView.clear()

    def controller_init_ca_algo(self):
        self._ca_algo = None
        self.deleted_ids = list()
        if not self.gbc_is_on:
            self.result_space = None
            self._ca_algo = CellularAutomata(int(self.lineEdit_number_of_grains.text()),
                                             int(self.lineEdit_inclusions_number.text()),
                                             int(self.lineEdit_min_radius.text()),
                                             int(self.lineEdit_max_radius.text()),
                                             int(self.lineEdit_size_of_space.text()),
                                             int(self.lineEdit_size_of_space.text()),
                                             str(self.comboBox_border_condition.currentText()),
                                             str(self.comboBox_neighbours_rule.currentText()))
            self._ca_algo.add_random()
            self._ca_algo.add_inclusions()
            self.view_generate_pg_colormap()
            self.view_generate_set_of_ids()
            self.view_display_image()
        else:
            self.result_space = None
            self._ca_algo = CellularAutomataGBC(int(self.lineEdit_number_of_grains.text()),
                                                int(self.lineEdit_inclusions_number.text()),
                                                int(self.lineEdit_min_radius.text()),
                                                int(self.lineEdit_max_radius.text()),
                                                int(self.lineEdit_size_of_space.text()),
                                                int(self.lineEdit_size_of_space.text()),
                                                str(self.comboBox_border_condition.currentText()),
                                                int(self.lineEdit_prob_threshold.text()))
            self._ca_algo.add_random()
            self._ca_algo.add_inclusions()
            self.view_generate_pg_colormap()
            self.view_generate_set_of_ids()
            self.view_display_image()

    def controller_init_image_timer(self):
        self.number_of_clicked += 1
        if self.number_of_clicked % 2:
            self.pushButton_start_stop.setStyleSheet("background-color: green")
            self.timer.timeout.connect(self.controller_update_func)
            self.timer.start(50)
        else:
            self.pushButton_start_stop.setStyleSheet("background-color: none")
            self.timer.stop()

    def controller_update_func(self):
        if self._ca_algo.cell_empty in self._ca_algo.space:
            if self.result_space is None:
                self.result_space = self.worker.apply_async(self._ca_algo.one_step)
                return

            if self.result_space.ready():
                self._ca_algo.space = self.result_space.get()
                self.view_display_image()
                self.result_space = self.worker.apply_async(self._ca_algo.one_step)
        else:
            self.comboBox_list_of_grains.setEnabled(True)
            self.pushButton_delete_grains.setEnabled(True)
            self.pushButton_keep_selected.setEnabled(True)

    def controller_one_step(self):
        self.timer.stop()
        self.controller_update_func()

    def controller_gbc_init(self):
        self.number_of_clicked_gbc += 1
        if self.number_of_clicked_gbc % 2:
            self.gbc_is_on = True
            self.pushButton_gbc_feature.setStyleSheet("background-color: green")
            self.comboBox_neighbours_rule.setCurrentText('MOORE')
            self.comboBox_neighbours_rule.setEnabled(False)
        else:
            self.gbc_is_on = False
            self.pushButton_gbc_feature.setStyleSheet("background-color: red")
            self.comboBox_neighbours_rule.setEnabled(True)

    def controller_init_substructures(self):
        kept_ids = self._ca_algo.list_of_id
        for one_id in self.deleted_ids:
            kept_ids.remove(one_id)
        for one_id in kept_ids:
            self._ca_algo.grain_model[one_id] = self._ca_algo.phase_nonzero
            self._ca_algo.color_id[one_id] = self._ca_algo.color_id[2]
        self.result_space = None
        self.view_display_image()

    def controller_init_dual_phase(self):
        kept_ids = self._ca_algo.list_of_id
        for one_id in self.deleted_ids:
            kept_ids.remove(one_id)
        # for one_id in kept_ids:
        #     self._ca_algo.grain_model[one_id] = self._ca_algo.phase_nonzero
        #     self._ca_algo.color_id[one_id] = self._ca_algo.color_id[2]
        for one_id in kept_ids:
            self._ca_algo.space[self._ca_algo.space == one_id] = 2
        self.result_space = None
        self.view_display_image()

    def controller_dual_phase_init(self):
        self._ca_algo.add_random_dual_phase()
        self.result_space = None
        self.view_display_image()

    def io_open_save_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.centralwidget, "Save to CSV file", "",
                                                  "CSV Files (*.csv)", options=options)
        if fileName:
            pd.DataFrame(self._ca_algo.space).to_csv(fileName)

    def io_open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.centralwidget, "Open CSV file", "",
                                                  "CSV Files (*.csv)", options=options)
        if fileName:
            self._ca_algo.space = pd.read_csv(fileName, index_col=0).astype(int).values
            self.view_display_image()

    def io_open_save_dialog_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.centralwidget, "Save to PNG file", "",
                                                  "PNG Files (*.png)", options=options)
        if fileName:
            self.graphicsView.export(fileName)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
