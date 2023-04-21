# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 683)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_scanner_id = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_scanner_id.setFont(font)
        self.label_scanner_id.setObjectName("label_scanner_id")
        self.horizontalLayout_2.addWidget(self.label_scanner_id)
        self.line_scanner_id = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_scanner_id.setFont(font)
        self.line_scanner_id.setObjectName("line_scanner_id")
        self.horizontalLayout_2.addWidget(self.line_scanner_id)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_save_folder = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_save_folder.setFont(font)
        self.label_save_folder.setObjectName("label_save_folder")
        self.horizontalLayout_4.addWidget(self.label_save_folder)
        self.line_save_folder = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_save_folder.setFont(font)
        self.line_save_folder.setReadOnly(True)
        self.line_save_folder.setObjectName("line_save_folder")
        self.horizontalLayout_4.addWidget(self.line_save_folder)
        self.button_select_folder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_select_folder.setObjectName("button_select_folder")
        self.horizontalLayout_4.addWidget(self.button_select_folder)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ip = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout.addWidget(self.label_ip)
        self.line_scanner_ip = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_scanner_ip.setFont(font)
        self.line_scanner_ip.setObjectName("line_scanner_ip")
        self.horizontalLayout.addWidget(self.line_scanner_ip)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_qr = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_qr.setFont(font)
        self.label_qr.setObjectName("label_qr")
        self.horizontalLayout_3.addWidget(self.label_qr)
        self.line_qr = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_qr.setFont(font)
        self.line_qr.setObjectName("line_qr")
        self.horizontalLayout_3.addWidget(self.line_qr)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ratio_connect = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.ratio_connect.setEnabled(False)
        self.ratio_connect.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.ratio_connect.setText("")
        self.ratio_connect.setObjectName("ratio_connect")
        self.horizontalLayout_6.addWidget(self.ratio_connect)
        self.button_connect = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_connect.setFont(font)
        self.button_connect.setObjectName("button_connect")
        self.horizontalLayout_6.addWidget(self.button_connect)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_7.addWidget(self.radioButton_2)
        self.button_qr_connect = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_qr_connect.setFont(font)
        self.button_qr_connect.setObjectName("button_qr_connect")
        self.horizontalLayout_7.addWidget(self.button_qr_connect)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_movement = QtWidgets.QWidget()
        self.tab_movement.setObjectName("tab_movement")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_movement)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_20 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_7.addWidget(self.label_20)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_23 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 1, 0, 1, 1)
        self.spinbox_currentZ = QtWidgets.QDoubleSpinBox(parent=self.tab_movement)
        self.spinbox_currentZ.setReadOnly(True)
        self.spinbox_currentZ.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_currentZ.setMinimum(-1000000.0)
        self.spinbox_currentZ.setMaximum(1000000.0)
        self.spinbox_currentZ.setObjectName("spinbox_currentZ")
        self.gridLayout_2.addWidget(self.spinbox_currentZ, 2, 1, 1, 1)
        self.spinbox_currentY = QtWidgets.QDoubleSpinBox(parent=self.tab_movement)
        self.spinbox_currentY.setReadOnly(True)
        self.spinbox_currentY.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_currentY.setMinimum(-1000000.0)
        self.spinbox_currentY.setMaximum(1000000.0)
        self.spinbox_currentY.setObjectName("spinbox_currentY")
        self.gridLayout_2.addWidget(self.spinbox_currentY, 1, 1, 1, 1)
        self.spinbox_currentX = QtWidgets.QDoubleSpinBox(parent=self.tab_movement)
        self.spinbox_currentX.setFrame(True)
        self.spinbox_currentX.setReadOnly(True)
        self.spinbox_currentX.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_currentX.setMinimum(-1000000.0)
        self.spinbox_currentX.setMaximum(1000000.0)
        self.spinbox_currentX.setObjectName("spinbox_currentX")
        self.gridLayout_2.addWidget(self.spinbox_currentX, 0, 1, 1, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.tab_movement)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.spinbox_stepY = QtWidgets.QDoubleSpinBox(parent=self.tab_movement)
        self.spinbox_stepY.setMinimum(0.0)
        self.spinbox_stepY.setMaximum(100000.0)
        self.spinbox_stepY.setObjectName("spinbox_stepY")
        self.gridLayout_3.addWidget(self.spinbox_stepY, 1, 1, 1, 1)
        self.spinbox_stepX = QtWidgets.QDoubleSpinBox(parent=self.tab_movement)
        self.spinbox_stepX.setMinimum(0.0)
        self.spinbox_stepX.setMaximum(100000.0)
        self.spinbox_stepX.setObjectName("spinbox_stepX")
        self.gridLayout_3.addWidget(self.spinbox_stepX, 0, 1, 1, 1)
        self.spinbox_stepZ = QtWidgets.QDoubleSpinBox(parent=self.tab_movement)
        self.spinbox_stepZ.setMinimum(0.0)
        self.spinbox_stepZ.setMaximum(100000.0)
        self.spinbox_stepZ.setObjectName("spinbox_stepZ")
        self.gridLayout_3.addWidget(self.spinbox_stepZ, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(parent=self.tab_movement)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_10.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_movement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.button_move_up = QtWidgets.QPushButton(parent=self.tab_movement)
        self.button_move_up.setObjectName("button_move_up")
        self.verticalLayout_4.addWidget(self.button_move_up)
        self.button_move_down = QtWidgets.QPushButton(parent=self.tab_movement)
        self.button_move_down.setObjectName("button_move_down")
        self.verticalLayout_4.addWidget(self.button_move_down)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.line_2 = QtWidgets.QFrame(parent=self.tab_movement)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_10.addWidget(self.line_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.button_move_left = QtWidgets.QPushButton(parent=self.tab_movement)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_move_left.setFont(font)
        self.button_move_left.setObjectName("button_move_left")
        self.verticalLayout_5.addWidget(self.button_move_left)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_move_counter_clockwise = QtWidgets.QPushButton(parent=self.tab_movement)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_move_counter_clockwise.setFont(font)
        self.button_move_counter_clockwise.setObjectName("button_move_counter_clockwise")
        self.horizontalLayout_9.addWidget(self.button_move_counter_clockwise)
        self.button_move_clockwise = QtWidgets.QPushButton(parent=self.tab_movement)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_move_clockwise.setFont(font)
        self.button_move_clockwise.setObjectName("button_move_clockwise")
        self.horizontalLayout_9.addWidget(self.button_move_clockwise)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.button_move_right = QtWidgets.QPushButton(parent=self.tab_movement)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_move_right.setFont(font)
        self.button_move_right.setObjectName("button_move_right")
        self.verticalLayout_5.addWidget(self.button_move_right)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.line_3 = QtWidgets.QFrame(parent=self.tab_movement)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_10.addWidget(self.line_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_movement)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.button_detect = QtWidgets.QPushButton(parent=self.tab_movement)
        self.button_detect.setObjectName("button_detect")
        self.verticalLayout_6.addWidget(self.button_detect)
        self.button_stop = QtWidgets.QPushButton(parent=self.tab_movement)
        self.button_stop.setObjectName("button_stop")
        self.verticalLayout_6.addWidget(self.button_stop)
        self.button_save_image = QtWidgets.QPushButton(parent=self.tab_movement)
        self.button_save_image.setObjectName("button_save_image")
        self.verticalLayout_6.addWidget(self.button_save_image)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_movement, "")
        self.tab_casset = QtWidgets.QWidget()
        self.tab_casset.setObjectName("tab_casset")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_casset)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_casset)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(parent=self.tab_casset)
        self.doubleSpinBox_7.setReadOnly(True)
        self.doubleSpinBox_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleSpinBox_7.setMinimum(-100000.0)
        self.doubleSpinBox_7.setMaximum(100000.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_6.addWidget(self.doubleSpinBox_7, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.tab_casset)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 0, 1, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(parent=self.tab_casset)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.horizontalLayout_17.addWidget(self.doubleSpinBox_8)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_casset)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_17.addWidget(self.pushButton_3)
        self.gridLayout_6.addLayout(self.horizontalLayout_17, 1, 1, 1, 1)
        self.horizontalLayout_18.addLayout(self.gridLayout_6)
        self.tabWidget.addTab(self.tab_casset, "")
        self.tab_z_stacks = QtWidgets.QWidget()
        self.tab_z_stacks.setObjectName("tab_z_stacks")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_z_stacks)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.button_move_up_Z = QtWidgets.QPushButton(parent=self.tab_z_stacks)
        self.button_move_up_Z.setObjectName("button_move_up_Z")
        self.gridLayout_4.addWidget(self.button_move_up_Z, 0, 1, 1, 1)
        self.checkBox_save = QtWidgets.QCheckBox(parent=self.tab_z_stacks)
        self.checkBox_save.setObjectName("checkBox_save")
        self.gridLayout_4.addWidget(self.checkBox_save, 0, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.tab_z_stacks)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.tab_z_stacks)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 3, 1, 1)
        self.button_move_down_Z = QtWidgets.QPushButton(parent=self.tab_z_stacks)
        self.button_move_down_Z.setObjectName("button_move_down_Z")
        self.gridLayout_4.addWidget(self.button_move_down_Z, 0, 2, 1, 1)
        self.spinbox_current_Z = QtWidgets.QDoubleSpinBox(parent=self.tab_z_stacks)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spinbox_current_Z.setFont(font)
        self.spinbox_current_Z.setReadOnly(True)
        self.spinbox_current_Z.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_current_Z.setMinimum(-100000.0)
        self.spinbox_current_Z.setMaximum(100000.0)
        self.spinbox_current_Z.setObjectName("spinbox_current_Z")
        self.gridLayout_4.addWidget(self.spinbox_current_Z, 1, 0, 1, 1)
        self.spinbox_move_up_Z = QtWidgets.QDoubleSpinBox(parent=self.tab_z_stacks)
        self.spinbox_move_up_Z.setMaximum(1000000.0)
        self.spinbox_move_up_Z.setObjectName("spinbox_move_up_Z")
        self.gridLayout_4.addWidget(self.spinbox_move_up_Z, 1, 1, 1, 1)
        self.spinbox_move_down_Z = QtWidgets.QDoubleSpinBox(parent=self.tab_z_stacks)
        self.spinbox_move_down_Z.setMaximum(10000000.0)
        self.spinbox_move_down_Z.setObjectName("spinbox_move_down_Z")
        self.gridLayout_4.addWidget(self.spinbox_move_down_Z, 1, 2, 1, 1)
        self.spinbox_step = QtWidgets.QDoubleSpinBox(parent=self.tab_z_stacks)
        self.spinbox_step.setMaximum(100000000.0)
        self.spinbox_step.setObjectName("spinbox_step")
        self.gridLayout_4.addWidget(self.spinbox_step, 1, 3, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_z_stacks, "")
        self.tab_autofocus = QtWidgets.QWidget()
        self.tab_autofocus.setObjectName("tab_autofocus")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_autofocus)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tabWidget.addTab(self.tab_autofocus, "")
        self.tab_traject = QtWidgets.QWidget()
        self.tab_traject.setObjectName("tab_traject")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_traject)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox = QtWidgets.QCheckBox(parent=self.tab_traject)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 0, 3, 1, 1)
        self.button_start_traject = QtWidgets.QPushButton(parent=self.tab_traject)
        self.button_start_traject.setObjectName("button_start_traject")
        self.gridLayout_5.addWidget(self.button_start_traject, 1, 3, 1, 1)
        self.button_load_traject = QtWidgets.QPushButton(parent=self.tab_traject)
        self.button_load_traject.setObjectName("button_load_traject")
        self.gridLayout_5.addWidget(self.button_load_traject, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.tab_traject)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 1, 1, 1)
        self.spinbox_traject_time = QtWidgets.QDoubleSpinBox(parent=self.tab_traject)
        self.spinbox_traject_time.setReadOnly(True)
        self.spinbox_traject_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox_traject_time.setObjectName("spinbox_traject_time")
        self.gridLayout_5.addWidget(self.spinbox_traject_time, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.tab_traject)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 2, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.spinbox_trajectX_speed = QtWidgets.QDoubleSpinBox(parent=self.tab_traject)
        self.spinbox_trajectX_speed.setObjectName("spinbox_trajectX_speed")
        self.horizontalLayout_16.addWidget(self.spinbox_trajectX_speed)
        self.spinbox_trajectY_speed = QtWidgets.QDoubleSpinBox(parent=self.tab_traject)
        self.spinbox_trajectY_speed.setObjectName("spinbox_trajectY_speed")
        self.horizontalLayout_16.addWidget(self.spinbox_trajectY_speed)
        self.gridLayout_5.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)
        self.label_current_file = QtWidgets.QLabel(parent=self.tab_traject)
        self.label_current_file.setObjectName("label_current_file")
        self.gridLayout_5.addWidget(self.label_current_file, 0, 0, 1, 1)
        self.horizontalLayout_13.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab_traject, "")
        self.tab_sensors = QtWidgets.QWidget()
        self.tab_sensors.setObjectName("tab_sensors")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab_sensors)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.tabWidget.addTab(self.tab_sensors, "")
        self.tab_camera = QtWidgets.QWidget()
        self.tab_camera.setObjectName("tab_camera")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_camera)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_17 = QtWidgets.QLabel(parent=self.tab_camera)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.tab_camera)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)
        self.spinbox_gamma = QtWidgets.QDoubleSpinBox(parent=self.tab_camera)
        self.spinbox_gamma.setMinimum(20.0)
        self.spinbox_gamma.setMaximum(180.0)
        self.spinbox_gamma.setObjectName("spinbox_gamma")
        self.gridLayout_7.addWidget(self.spinbox_gamma, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self.tab_camera)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 1, 0, 1, 1)
        self.spinbox_contrast = QtWidgets.QDoubleSpinBox(parent=self.tab_camera)
        self.spinbox_contrast.setMinimum(-100.0)
        self.spinbox_contrast.setMaximum(100.0)
        self.spinbox_contrast.setObjectName("spinbox_contrast")
        self.gridLayout_7.addWidget(self.spinbox_contrast, 1, 1, 1, 1)
        self.spinbox_exposure_time = QtWidgets.QDoubleSpinBox(parent=self.tab_camera)
        self.spinbox_exposure_time.setMinimum(-1000000.0)
        self.spinbox_exposure_time.setMaximum(1000000.0)
        self.spinbox_exposure_time.setObjectName("spinbox_exposure_time")
        self.gridLayout_7.addWidget(self.spinbox_exposure_time, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.tab_camera)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(parent=self.tab_camera)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 0, 2, 1, 1)
        self.spinbox_brightness = QtWidgets.QDoubleSpinBox(parent=self.tab_camera)
        self.spinbox_brightness.setMinimum(-64.0)
        self.spinbox_brightness.setMaximum(64.0)
        self.spinbox_brightness.setObjectName("spinbox_brightness")
        self.gridLayout_7.addWidget(self.spinbox_brightness, 3, 1, 1, 1)
        self.spindbox_resolution = QtWidgets.QDoubleSpinBox(parent=self.tab_camera)
        self.spindbox_resolution.setMinimum(-1000000.0)
        self.spindbox_resolution.setMaximum(1000000.0)
        self.spindbox_resolution.setObjectName("spindbox_resolution")
        self.gridLayout_7.addWidget(self.spindbox_resolution, 0, 3, 1, 1)
        self.button_save_camera = QtWidgets.QPushButton(parent=self.tab_camera)
        self.button_save_camera.setObjectName("button_save_camera")
        self.gridLayout_7.addWidget(self.button_save_camera, 3, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(parent=self.tab_camera)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 1, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(parent=self.tab_camera)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 2, 2, 1, 1)
        self.spinbox_hue = QtWidgets.QDoubleSpinBox(parent=self.tab_camera)
        self.spinbox_hue.setMinimum(-180.0)
        self.spinbox_hue.setMaximum(180.0)
        self.spinbox_hue.setObjectName("spinbox_hue")
        self.gridLayout_7.addWidget(self.spinbox_hue, 1, 3, 1, 1)
        self.spinbox_imtemp = QtWidgets.QDoubleSpinBox(parent=self.tab_camera)
        self.spinbox_imtemp.setObjectName("spinbox_imtemp")
        self.gridLayout_7.addWidget(self.spinbox_imtemp, 2, 3, 1, 1)
        self.horizontalLayout_15.addLayout(self.gridLayout_7)
        self.tabWidget.addTab(self.tab_camera, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 578, 366))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Frame = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.Frame.setText("")
        self.Frame.setObjectName("Frame")
        self.verticalLayout_9.addWidget(self.Frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.addWidget(self.scrollArea)
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_5.addWidget(self.line_4)
        self.listView_log = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listView_log.setObjectName("listView_log")
        self.horizontalLayout_5.addWidget(self.listView_log)
        self.horizontalLayout_5.setStretch(0, 7)
        self.horizontalLayout_5.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_10 = QtGui.QAction(parent=MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_scanner_id.setText(_translate("MainWindow", "ID сканера"))
        self.label_save_folder.setText(_translate("MainWindow", "Папка сохранения:"))
        self.button_select_folder.setText(_translate("MainWindow", "Выбрать"))
        self.label_ip.setText(_translate("MainWindow", "IP сканера:"))
        self.label_qr.setText(_translate("MainWindow", "Штрих-код:"))
        self.button_connect.setText(_translate("MainWindow", "Подключить"))
        self.button_qr_connect.setText(_translate("MainWindow", "Сканер штрих-кода"))
        self.label_20.setText(_translate("MainWindow", "Текущие координаты"))
        self.label_23.setText(_translate("MainWindow", "Z"))
        self.label_21.setText(_translate("MainWindow", "X"))
        self.label_22.setText(_translate("MainWindow", "Y"))
        self.label.setText(_translate("MainWindow", "Шаг"))
        self.label_7.setText(_translate("MainWindow", "Z"))
        self.label_6.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Объектив"))
        self.button_move_up.setText(_translate("MainWindow", "↑"))
        self.button_move_down.setText(_translate("MainWindow", "↓"))
        self.label_3.setText(_translate("MainWindow", "Препарат"))
        self.button_move_left.setText(_translate("MainWindow", "←"))
        self.button_move_counter_clockwise.setText(_translate("MainWindow", "⤿"))
        self.button_move_clockwise.setText(_translate("MainWindow", "⤾"))
        self.button_move_right.setText(_translate("MainWindow", "→"))
        self.label_4.setText(_translate("MainWindow", "Изображение"))
        self.button_detect.setText(_translate("MainWindow", "Детектировать"))
        self.button_stop.setText(_translate("MainWindow", "Остановить"))
        self.button_save_image.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_movement), _translate("MainWindow", "Перемещение"))
        self.label_13.setText(_translate("MainWindow", "Текущая позиция"))
        self.label_14.setText(_translate("MainWindow", "Переместить в позицию"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_casset), _translate("MainWindow", "Кассета"))
        self.button_move_up_Z.setText(_translate("MainWindow", "Подняться по Z на"))
        self.checkBox_save.setText(_translate("MainWindow", "Сохранять изображения"))
        self.label_8.setText(_translate("MainWindow", "Текущая позиция"))
        self.label_9.setText(_translate("MainWindow", "Шаг"))
        self.button_move_down_Z.setText(_translate("MainWindow", "Спуситься по Z на"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_z_stacks), _translate("MainWindow", "Z-стеки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_autofocus), _translate("MainWindow", "Автофокусировка"))
        self.checkBox.setText(_translate("MainWindow", "Сохранять изображения"))
        self.button_start_traject.setText(_translate("MainWindow", "Выполнить"))
        self.button_load_traject.setText(_translate("MainWindow", "Выбрать файл"))
        self.label_11.setText(_translate("MainWindow", "Скорость по X и Y"))
        self.label_12.setText(_translate("MainWindow", "Время перемещения"))
        self.label_current_file.setText(_translate("MainWindow", "Текущий файл: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_traject), _translate("MainWindow", "Траектория"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sensors), _translate("MainWindow", "Датчики"))
        self.label_17.setText(_translate("MainWindow", "Время экспозиции"))
        self.label_15.setText(_translate("MainWindow", "Гамма"))
        self.label_16.setText(_translate("MainWindow", "Контрастность"))
        self.label_18.setText(_translate("MainWindow", "Яркость"))
        self.label_19.setText(_translate("MainWindow", "Разрешение"))
        self.button_save_camera.setText(_translate("MainWindow", "Применить"))
        self.label_24.setText(_translate("MainWindow", "HUE"))
        self.label_25.setText(_translate("MainWindow", "Цветовая температура"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camera), _translate("MainWindow", "Камера"))
        self.action_7.setText(_translate("MainWindow", "Перевод в 7"))
        self.action_10.setText(_translate("MainWindow", "Перевод в 10"))
        self.action_2.setText(_translate("MainWindow", "Очистить ввод"))
        self.action_3.setText(_translate("MainWindow", "Очистить вывод"))
        self.action_4.setText(_translate("MainWindow", "Очистить все"))
