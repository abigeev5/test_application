from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from datetime import datetime
from PIL import Image
import numpy as np
import argparse
import sys, os
import json
import cv2

from utils import Scanner, Barcode_scanner
from inference import Inference


class Ui_Dialog(QtWidgets.QWidget):
    bar_signal = QtCore.pyqtSignal(str)
    video_signal = QtCore.pyqtSignal(bytes)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1012, 800)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 981, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_moving = QtWidgets.QWidget()
        self.tab_moving.setObjectName("tab_moving")
        self.groupBox_parameters = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_parameters.setGeometry(QtCore.QRect(0, 10, 291, 201))
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        self.label_X = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_X.setGeometry(QtCore.QRect(30, 40, 55, 31))
        self.label_X.setObjectName("label_X")
        self.label_Y = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_Y.setGeometry(QtCore.QRect(30, 80, 55, 31))
        self.label_Y.setObjectName("label_Y")
        self.label_Z = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_Z.setGeometry(QtCore.QRect(30, 120, 55, 31))
        self.label_Z.setObjectName("label_Z")
        self.label_Speed = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_Speed.setGeometry(QtCore.QRect(90, 10, 55, 16))
        self.label_Speed.setObjectName("label_Speed")
        self.label_acceleration = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_acceleration.setGeometry(QtCore.QRect(190, 10, 61, 16))
        self.label_acceleration.setObjectName("label_acceleration")
        self.lineEdit_speedX = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.lineEdit_speedX.setGeometry(QtCore.QRect(70, 40, 81, 22))
        self.lineEdit_speedX.setObjectName("lineEdit_speedX")
        self.lineEdit_speedY = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.lineEdit_speedY.setGeometry(QtCore.QRect(70, 80, 81, 22))
        self.lineEdit_speedY.setObjectName("lineEdit_speedY")
        self.lineEdit_speedZ = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.lineEdit_speedZ.setGeometry(QtCore.QRect(70, 120, 81, 22))
        self.lineEdit_speedZ.setObjectName("lineEdit_speedZ")
        self.lineEdit_accX = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.lineEdit_accX.setGeometry(QtCore.QRect(180, 40, 81, 22))
        self.lineEdit_accX.setObjectName("lineEdit_accX")
        self.lineEdit_accY = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.lineEdit_accY.setGeometry(QtCore.QRect(180, 80, 81, 22))
        self.lineEdit_accY.setObjectName("lineEdit_accY")
        self.lineEdit_accZ = QtWidgets.QSpinBox(self.groupBox_parameters)
        self.lineEdit_accZ.setGeometry(QtCore.QRect(180, 120, 81, 22))
        self.lineEdit_accZ.setObjectName("lineEdit_accZ")
        self.groupBox_moving = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_moving.setGeometry(QtCore.QRect(300, 10, 171, 201))
        self.groupBox_moving.setObjectName("groupBox_moving")
        self.radioButton_X = QtWidgets.QRadioButton(self.groupBox_moving)
        self.radioButton_X.setGeometry(QtCore.QRect(30, 40, 95, 21))
        self.radioButton_X.setText("")
        self.radioButton_X.setObjectName("radioButton_X")
        self.radioButton_Y = QtWidgets.QRadioButton(self.groupBox_moving)
        self.radioButton_Y.setGeometry(QtCore.QRect(30, 80, 95, 21))
        self.radioButton_Y.setText("")
        self.radioButton_Y.setObjectName("radioButton_Y")
        self.radioButton_Z = QtWidgets.QRadioButton(self.groupBox_moving)
        self.radioButton_Z.setGeometry(QtCore.QRect(30, 120, 95, 21))
        self.radioButton_Z.setText("")
        self.radioButton_Z.setObjectName("radioButton_Z")
        self.pushButton_move = QtWidgets.QPushButton(self.groupBox_moving)
        self.pushButton_move.setGeometry(QtCore.QRect(72, 160, 91, 31))
        self.pushButton_move.setObjectName("pushButton_move")
        self.lineEdit_moveY = QtWidgets.QSpinBox(self.groupBox_moving)
        self.lineEdit_moveY.setGeometry(QtCore.QRect(60, 80, 81, 22))
        self.lineEdit_moveY.setObjectName("lineEdit_moveY")
        self.lineEdit_moveZ = QtWidgets.QSpinBox(self.groupBox_moving)
        self.lineEdit_moveZ.setGeometry(QtCore.QRect(60, 120, 81, 22))
        self.lineEdit_moveZ.setObjectName("lineEdit_moveZ")
        self.lineEdit_moveX = QtWidgets.QSpinBox(self.groupBox_moving)
        self.lineEdit_moveX.setGeometry(QtCore.QRect(60, 40, 81, 22))
        self.lineEdit_moveX.setObjectName("lineEdit_moveX")
        self.pushButton_move_0 = QtWidgets.QPushButton(self.groupBox_moving)
        self.pushButton_move_0.setGeometry(QtCore.QRect(10, 160, 61, 31))
        self.pushButton_move_0.setObjectName("pushButton_move_0")
        self.groupBox_objective = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_objective.setGeometry(QtCore.QRect(480, 10, 111, 201))
        self.groupBox_objective.setObjectName("groupBox_objective")
        self.pushButton_up = QtWidgets.QPushButton(self.groupBox_objective)
        self.pushButton_up.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.pushButton_up.setObjectName("pushButton_up")
        self.pushButton_down = QtWidgets.QPushButton(self.groupBox_objective)
        self.pushButton_down.setGeometry(QtCore.QRect(10, 90, 93, 28))
        self.pushButton_down.setObjectName("pushButton_down")
        self.groupBox_product = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_product.setGeometry(QtCore.QRect(600, 10, 201, 201))
        self.groupBox_product.setObjectName("groupBox_product")
        self.pushButton_product_left = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_left.setGeometry(QtCore.QRect(10, 60, 61, 28))
        self.pushButton_product_left.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_product_left.setIcon(icon)
        self.pushButton_product_left.setObjectName("pushButton_product_left")
        self.pushButton_product_right = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_right.setGeometry(QtCore.QRect(130, 60, 61, 28))
        self.pushButton_product_right.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_product_right.setIcon(icon1)
        self.pushButton_product_right.setObjectName("pushButton_product_right")
        self.pushButton_product_up = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_up.setGeometry(QtCore.QRect(70, 30, 61, 28))
        self.pushButton_product_up.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_product_up.setIcon(icon2)
        self.pushButton_product_up.setObjectName("pushButton_product_up")
        self.pushButton_product_down = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_down.setGeometry(QtCore.QRect(70, 90, 61, 28))
        self.pushButton_product_down.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_product_down.setIcon(icon3)
        self.pushButton_product_down.setObjectName("pushButton_product_down")
        self.groupBox_image = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_image.setGeometry(QtCore.QRect(810, 10, 151, 201))
        self.groupBox_image.setObjectName("groupBox_image")
        self.pushButton_imageSave = QtWidgets.QPushButton(self.groupBox_image)
        self.pushButton_imageSave.setGeometry(QtCore.QRect(30, 160, 101, 28))
        self.pushButton_imageSave.setObjectName("pushButton_imageSave")
        self.pushButton_imageDetect = QtWidgets.QPushButton(self.groupBox_image)
        self.pushButton_imageDetect.setGeometry(QtCore.QRect(30, 100, 101, 28))
        self.pushButton_imageDetect.setObjectName("pushButton_imageDetect")
        self.pushButton_imageStop = QtWidgets.QPushButton(self.groupBox_image)
        self.pushButton_imageStop.setGeometry(QtCore.QRect(30, 40, 101, 28))
        self.pushButton_imageStop.setObjectName("pushButton_imageStop")
        self.listView_current_coordinate = QtWidgets.QListWidget(self.tab_moving)
        self.listView_current_coordinate.setGeometry(QtCore.QRect(610, 240, 341, 351))
        self.listView_current_coordinate.setObjectName("listView_current_coordinate")
        self.label_current_coordinate = QtWidgets.QLabel(self.tab_moving)
        self.label_current_coordinate.setGeometry(QtCore.QRect(730, 220, 151, 16))
        self.label_current_coordinate.setObjectName("label_current_coordinate")
        self.verticalScrollBar_current_coordinate = QtWidgets.QScrollBar(self.tab_moving)
        self.verticalScrollBar_current_coordinate.setGeometry(QtCore.QRect(950, 220, 16, 371))
        self.verticalScrollBar_current_coordinate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_current_coordinate.setObjectName("verticalScrollBar_current_coordinate")
        
        self.frame_large = QtWidgets.QLabel()
        self.frame_large.setGeometry(QtCore.QRect(10, 219, 581, 371))
        self.frame_large.setObjectName("frame_large")
        
        self.area = QtWidgets.QScrollArea(self.tab_moving)
        self.area.setGeometry(QtCore.QRect(10, 219, 581, 371))
        self.area.setWidget(self.frame_large)
        
        self.tabWidget.addTab(self.tab_moving, "")
        self.tab_casset = QtWidgets.QWidget()
        self.tab_casset.setObjectName("tab_casset")
        self.groupBox_position = QtWidgets.QGroupBox(self.tab_casset)
        self.groupBox_position.setGeometry(QtCore.QRect(10, 10, 951, 71))
        self.groupBox_position.setObjectName("groupBox_position")
        self.label_ipscaner_current_position = QtWidgets.QLabel(self.groupBox_position)
        self.label_ipscaner_current_position.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.label_ipscaner_current_position.setObjectName("label_ipscaner_current_position")
        self.label_ipscaner_3 = QtWidgets.QLabel(self.groupBox_position)
        self.label_ipscaner_3.setGeometry(QtCore.QRect(180, 20, 151, 16))
        self.label_ipscaner_3.setObjectName("label_ipscaner_3")
        self.pushButton_change_position = QtWidgets.QPushButton(self.groupBox_position)
        self.pushButton_change_position.setGeometry(QtCore.QRect(330, 30, 111, 31))
        self.pushButton_change_position.setObjectName("pushButton_change_position")
        self.lineEdit_CurrentPosition = QtWidgets.QLineEdit(self.groupBox_position)
        self.lineEdit_CurrentPosition.setGeometry(QtCore.QRect(70, 40, 71, 22))
        self.lineEdit_CurrentPosition.setObjectName("lineEdit_CurrentPosition")
        self.lineEdit_moveToPosition = QtWidgets.QLineEdit(self.groupBox_position)
        self.lineEdit_moveToPosition.setGeometry(QtCore.QRect(220, 40, 71, 22))
        self.lineEdit_moveToPosition.setObjectName("lineEdit_moveToPosition")
        self.frame = QtWidgets.QFrame(self.tab_casset)
        self.frame.setGeometry(QtCore.QRect(9, 89, 951, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.tab_casset, "")
        self.tab_z_stack = QtWidgets.QWidget()
        self.tab_z_stack.setObjectName("tab_z_stack")
        self.groupBox = QtWidgets.QGroupBox(self.tab_z_stack)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 951, 91))
        self.groupBox.setObjectName("groupBox")
        self.checkBox_save_z_stack = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_save_z_stack.setGeometry(QtCore.QRect(480, 30, 201, 21))
        self.checkBox_save_z_stack.setObjectName("checkBox_save_z_stack")
        self.label_current_z = QtWidgets.QLabel(self.groupBox)
        self.label_current_z.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label_current_z.setObjectName("label_current_z")
        self.lineEdit_currentZ = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_currentZ.setGeometry(QtCore.QRect(30, 50, 61, 22))
        self.lineEdit_currentZ.setObjectName("lineEdit_currentZ")
        self.lineEdit_up_to_Z = QtWidgets.QSpinBox(self.groupBox)
        self.lineEdit_up_to_Z.setGeometry(QtCore.QRect(160, 50, 61, 22))
        self.lineEdit_up_to_Z.setObjectName("lineEdit_up_to_Z")
        self.lineEdit_down_to_Z = QtWidgets.QSpinBox(self.groupBox)
        self.lineEdit_down_to_Z.setGeometry(QtCore.QRect(280, 50, 61, 22))
        self.lineEdit_down_to_Z.setObjectName("lineEdit_down_to_Z")
        self.lineEdit_step_Z = QtWidgets.QSpinBox(self.groupBox)
        self.lineEdit_step_Z.setGeometry(QtCore.QRect(370, 50, 61, 22))
        self.lineEdit_step_Z.setObjectName("lineEdit_step_Z")
        self.pushButton_UpByZ = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_UpByZ.setGeometry(QtCore.QRect(130, 20, 111, 28))
        self.pushButton_UpByZ.setObjectName("pushButton_UpByZ")
        self.pushButton_downByZ = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_downByZ.setGeometry(QtCore.QRect(250, 20, 111, 28))
        self.pushButton_downByZ.setObjectName("pushButton_downByZ")
        self.label_step = QtWidgets.QLabel(self.groupBox)
        self.label_step.setGeometry(QtCore.QRect(390, 30, 31, 16))
        self.label_step.setObjectName("label_step")
        self.frame_Z = QtWidgets.QFrame(self.tab_z_stack)
        self.frame_Z.setGeometry(QtCore.QRect(9, 119, 951, 481))
        self.frame_Z.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Z.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Z.setObjectName("frame_Z")
        self.tabWidget.addTab(self.tab_z_stack, "")
        self.tab_autofocus = QtWidgets.QWidget()
        self.tab_autofocus.setObjectName("tab_autofocus")
        self.tabWidget.addTab(self.tab_autofocus, "")
        self.tab_trajectory = QtWidgets.QWidget()
        self.tab_trajectory.setObjectName("tab_trajectory")
        self.groupBox_trajectory = QtWidgets.QGroupBox(self.tab_trajectory)
        self.groupBox_trajectory.setGeometry(QtCore.QRect(10, 10, 951, 111))
        self.groupBox_trajectory.setTitle("")
        self.groupBox_trajectory.setObjectName("groupBox_trajectory")
        self.checkBox_trajectory_save_image = QtWidgets.QCheckBox(self.groupBox_trajectory)
        self.checkBox_trajectory_save_image.setGeometry(QtCore.QRect(770, 30, 171, 17))
        self.checkBox_trajectory_save_image.setObjectName("checkBox_trajectory_save_image")
        self.pushButton_trajectory_execute = QtWidgets.QPushButton(self.groupBox_trajectory)
        self.pushButton_trajectory_execute.setGeometry(QtCore.QRect(800, 60, 111, 28))
        self.pushButton_trajectory_execute.setObjectName("pushButton_trajectory_execute")
        self.label_load_trajectory = QtWidgets.QLabel(self.groupBox_trajectory)
        self.label_load_trajectory.setGeometry(QtCore.QRect(340, 30, 111, 20))
        self.label_load_trajectory.setObjectName("label_load_trajectory")
        self.label_trajectory_speed = QtWidgets.QLabel(self.groupBox_trajectory)
        self.label_trajectory_speed.setGeometry(QtCore.QRect(40, 30, 201, 16))
        self.label_trajectory_speed.setObjectName("label_trajectory_speed")
        self.pushButton_load_trajectory = QtWidgets.QPushButton(self.groupBox_trajectory)
        self.pushButton_load_trajectory.setGeometry(QtCore.QRect(40, 50, 191, 31))
        self.pushButton_load_trajectory.setObjectName("pushButton_load_trajectory")
        self.lineEdit_sppedByX = QtWidgets.QLineEdit(self.groupBox_trajectory)
        self.lineEdit_sppedByX.setGeometry(QtCore.QRect(332, 60, 51, 22))
        self.lineEdit_sppedByX.setObjectName("lineEdit_sppedByX")
        self.lineEdit_speedByY = QtWidgets.QLineEdit(self.groupBox_trajectory)
        self.lineEdit_speedByY.setGeometry(QtCore.QRect(400, 60, 51, 22))
        self.lineEdit_speedByY.setObjectName("lineEdit_speedByY")
        self.label_trajectory_time = QtWidgets.QLabel(self.groupBox_trajectory)
        self.label_trajectory_time.setGeometry(QtCore.QRect(520, 30, 221, 20))
        self.label_trajectory_time.setObjectName("label_trajectory_time")
        self.lineEdit_trajectory_time = QtWidgets.QLineEdit(self.groupBox_trajectory)
        self.lineEdit_trajectory_time.setGeometry(QtCore.QRect(600, 60, 61, 22))
        self.lineEdit_trajectory_time.setObjectName("lineEdit_trajectory_time")
        self.listView_trajectory = QtWidgets.QListView(self.tab_trajectory)
        self.listView_trajectory.setGeometry(QtCore.QRect(680, 150, 256, 451))
        self.listView_trajectory.setObjectName("listView_trajectory")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.tab_trajectory)
        self.verticalScrollBar.setGeometry(QtCore.QRect(940, 150, 20, 451))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_trajectory_ = QtWidgets.QLabel(self.tab_trajectory)
        self.label_trajectory_.setGeometry(QtCore.QRect(740, 130, 141, 16))
        self.label_trajectory_.setObjectName("label_trajectory_")
        self.frame_trajectory = QtWidgets.QFrame(self.tab_trajectory)
        self.frame_trajectory.setGeometry(QtCore.QRect(9, 149, 661, 451))
        self.frame_trajectory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_trajectory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_trajectory.setObjectName("frame_trajectory")
        self.tabWidget.addTab(self.tab_trajectory, "")
        self.tab_sensor = QtWidgets.QWidget()
        self.tab_sensor.setObjectName("tab_sensor")
        self.tabWidget.addTab(self.tab_sensor, "")
        self.tab_camera = QtWidgets.QWidget()
        self.tab_camera.setObjectName("tab_camera")
        self.lineEdit_gamma = QtWidgets.QSpinBox(self.tab_camera)
        self.lineEdit_gamma.setGeometry(QtCore.QRect(130, 30, 61, 22))
        self.lineEdit_gamma.setObjectName("lineEdit_gamma")
        self.label_gamma = QtWidgets.QLabel(self.tab_camera)
        self.label_gamma.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.label_gamma.setObjectName("label_gamma")
        self.label_contrast = QtWidgets.QLabel(self.tab_camera)
        self.label_contrast.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_contrast.setObjectName("label_contrast")
        self.label_exposure_time = QtWidgets.QLabel(self.tab_camera)
        self.label_exposure_time.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.label_exposure_time.setObjectName("label_exposure_time")
        self.label_brightness = QtWidgets.QLabel(self.tab_camera)
        self.label_brightness.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.label_brightness.setObjectName("label_brightness")
        self.lineEdit_contrast = QtWidgets.QSpinBox(self.tab_camera)
        self.lineEdit_contrast.setGeometry(QtCore.QRect(130, 60, 61, 22))
        self.lineEdit_contrast.setObjectName("lineEdit_contrast")
        self.lineEdit_exposure_time = QtWidgets.QSpinBox(self.tab_camera)
        self.lineEdit_exposure_time.setGeometry(QtCore.QRect(130, 90, 61, 22))
        self.lineEdit_exposure_time.setObjectName("lineEdit_exposure_time")
        self.lineEdit_brightness = QtWidgets.QSpinBox(self.tab_camera)
        self.lineEdit_brightness.setGeometry(QtCore.QRect(130, 120, 61, 22))
        self.lineEdit_brightness.setObjectName("lineEdit_brightness")
        self.pushButton_set_settings = QtWidgets.QPushButton(self.tab_camera)
        self.pushButton_set_settings.setGeometry(QtCore.QRect(50, 160, 93, 28))
        self.pushButton_set_settings.setObjectName("pushButton_set_settings")
        self.tabWidget.addTab(self.tab_camera, "")
        self.groupBox_initial = QtWidgets.QGroupBox(Dialog)
        self.groupBox_initial.setGeometry(QtCore.QRect(20, 10, 981, 131))
        font = QtGui.QFont()
        font.setKerning(False)
        self.groupBox_initial.setFont(font)
        self.groupBox_initial.setObjectName("groupBox_initial")
        self.label_ipscaner = QtWidgets.QLabel(self.groupBox_initial)
        self.label_ipscaner.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.label_ipscaner.setObjectName("label_ipscaner")
        self.label_folder = QtWidgets.QLabel(self.groupBox_initial)
        self.label_folder.setGeometry(QtCore.QRect(10, 100, 111, 21))
        self.label_folder.setObjectName("label_folder")
        self.label_idscaner = QtWidgets.QLabel(self.groupBox_initial)
        self.label_idscaner.setGeometry(QtCore.QRect(490, 20, 71, 21))
        self.label_idscaner.setObjectName("label_idscaner")
        self.pushButton_connection = QtWidgets.QPushButton(self.groupBox_initial)
        self.pushButton_connection.setGeometry(QtCore.QRect(850, 20, 121, 28))
        self.pushButton_connection.setObjectName("pushButton_connection")
        self.pushButton_scaner = QtWidgets.QPushButton(self.groupBox_initial)
        self.pushButton_scaner.setGeometry(QtCore.QRect(852, 60, 121, 28))
        self.pushButton_scaner.setObjectName("pushButton_scaner")
        self.label_scaner_code = QtWidgets.QLabel(self.groupBox_initial)
        self.label_scaner_code.setGeometry(QtCore.QRect(30, 60, 71, 21))
        self.label_scaner_code.setObjectName("label_scaner_code")
        self.checkBox_scaner_code_file = QtWidgets.QCheckBox(self.groupBox_initial)
        self.checkBox_scaner_code_file.setGeometry(QtCore.QRect(490, 60, 181, 21))
        self.checkBox_scaner_code_file.setObjectName("checkBox_scaner_code_file")
        self.radioButton_Connection = QtWidgets.QRadioButton(self.groupBox_initial)
        self.radioButton_Connection.setEnabled(True)
        self.radioButton_Connection.setGeometry(QtCore.QRect(830, 20, 95, 31))
        self.radioButton_Connection.setMouseTracking(False)
        self.radioButton_Connection.setText("")
        self.radioButton_Connection.setObjectName("radioButton_Connection")
        self.radioButton_Code = QtWidgets.QRadioButton(self.groupBox_initial)
        self.radioButton_Code.setGeometry(QtCore.QRect(830, 60, 95, 31))
        self.radioButton_Code.setMouseTracking(False)
        self.radioButton_Code.setText("")
        self.radioButton_Code.setObjectName("radioButton_Code")
        self.lineEdit_ipScanner = QtWidgets.QLineEdit(self.groupBox_initial)
        self.lineEdit_ipScanner.setGeometry(QtCore.QRect(130, 20, 331, 22))
        self.lineEdit_ipScanner.setObjectName("lineEdit_ipScanner")
        self.lineEdit_scanerCode = QtWidgets.QLineEdit(self.groupBox_initial)
        self.lineEdit_scanerCode.setGeometry(QtCore.QRect(130, 60, 331, 22))
        self.lineEdit_scanerCode.setObjectName("lineEdit_scanerCode")
        self.lineEdit_path_to_save = QtWidgets.QLineEdit(self.groupBox_initial)
        self.lineEdit_path_to_save.setGeometry(QtCore.QRect(130, 100, 501, 22))
        self.lineEdit_path_to_save.setObjectName("lineEdit_path_to_save")
        self.lineEdit_idScanner = QtWidgets.QLineEdit(self.groupBox_initial)
        self.lineEdit_idScanner.setGeometry(QtCore.QRect(560, 20, 251, 22))
        self.lineEdit_idScanner.setObjectName("lineEdit_idScanner")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_initial)
        self.pushButton.setGeometry(QtCore.QRect(850, 100, 121, 28))
        self.pushButton.setObjectName("pushButton")

        self.set_listeners()
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.closeEvent = self.close_event
        self.config = {
            "stream_stopped": False,
            "bar_scanner": False,
            "scanner_connected": False,
            "video_stream": False,
            "speed_x": 1
        }

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Управление сканером препаратов")
        self.groupBox_parameters.setTitle(_translate("Dialog", "Параметры"))
        self.label_X.setText(_translate("Dialog", "X"))
        self.label_Y.setText(_translate("Dialog", "Y"))
        self.label_Z.setText(_translate("Dialog", "Z"))
        self.label_Speed.setText(_translate("Dialog", "Скорость"))
        self.label_acceleration.setText(_translate("Dialog", "Ускорение"))
        self.groupBox_moving.setTitle(_translate("Dialog", "Перемещение"))
        self.pushButton_move.setText(_translate("Dialog", "Переместить"))
        self.pushButton_move_0.setText(_translate("Dialog", "(0, 0, 0)"))
        self.groupBox_objective.setTitle(_translate("Dialog", "Объектив"))
        self.pushButton_up.setText(_translate("Dialog", "Вверх"))
        self.pushButton_down.setText(_translate("Dialog", "Вниз"))
        self.groupBox_product.setTitle(_translate("Dialog", "Препарат"))
        self.groupBox_image.setTitle(_translate("Dialog", "Изображение"))
        self.pushButton_imageSave.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_imageDetect.setText(_translate("Dialog", "Детектировать"))
        self.pushButton_imageStop.setText(_translate("Dialog", "Стоп"))
        self.label_current_coordinate.setText(_translate("Dialog", "Текущая координата"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_moving), _translate("Dialog", "Перемещение"))
        self.groupBox_position.setTitle(_translate("Dialog", "Позиция"))
        self.label_ipscaner_current_position.setText(_translate("Dialog", "Текущая позиция"))
        self.label_ipscaner_3.setText(_translate("Dialog", "Переместить в позицию"))
        self.pushButton_change_position.setText(_translate("Dialog", "Выполнить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_casset), _translate("Dialog", "Кассета"))
        self.groupBox.setTitle(_translate("Dialog", "Перемещение по z"))
        self.checkBox_save_z_stack.setText(_translate("Dialog", "сохранять все изображения"))
        self.label_current_z.setText(_translate("Dialog", "Текущее Z"))
        self.pushButton_UpByZ.setText(_translate("Dialog", "Подняться по Z"))
        self.pushButton_downByZ.setText(_translate("Dialog", "Спуститься по Z"))
        self.label_step.setText(_translate("Dialog", "Шаг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_z_stack), _translate("Dialog", "Z-стеки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_autofocus), _translate("Dialog", "Автофокусировка"))
        self.checkBox_trajectory_save_image.setText(_translate("Dialog", "сохранить изображения"))
        self.pushButton_trajectory_execute.setText(_translate("Dialog", "Выполнить"))
        self.label_load_trajectory.setText(_translate("Dialog", "Скорость по X и Y"))
        self.label_trajectory_speed.setText(_translate("Dialog", "Загрузить траекторию из файла"))
        self.pushButton_load_trajectory.setText(_translate("Dialog", "Выбрать файл"))
        self.label_trajectory_time.setText(_translate("Dialog", "Время перемещения по траектории"))
        self.label_trajectory_.setText(_translate("Dialog", "Движение по траектории"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_trajectory), _translate("Dialog", "По траектории"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sensor), _translate("Dialog", "Датчики"))
        self.label_gamma.setText(_translate("Dialog", "Гамма"))
        self.label_contrast.setText(_translate("Dialog", "Контраст"))
        self.label_exposure_time.setText(_translate("Dialog", "Вермя экспозиции"))
        self.label_brightness.setText(_translate("Dialog", "Яркость"))
        self.pushButton_set_settings.setText(_translate("Dialog", "Установить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camera), _translate("Dialog", "Камера"))
        self.groupBox_initial.setTitle(_translate("Dialog", "Параметры инициализации"))
        self.label_ipscaner.setText(_translate("Dialog", "IP Сканера"))
        self.label_folder.setText(_translate("Dialog", "Папка сохранения"))
        self.label_idscaner.setText(_translate("Dialog", "ID Сканера"))
        self.pushButton_connection.setText(_translate("Dialog", "Подключить"))
        self.pushButton_scaner.setText(_translate("Dialog", "Сканер ШтрихКода"))
        self.label_scaner_code.setText(_translate("Dialog", "Штрих-Код"))
        self.checkBox_scaner_code_file.setText(_translate("Dialog", "Сохранять в имени файла"))
        self.pushButton.setText(_translate("Dialog", "Выбрать папку"))
        
    def set_listeners(self):
        global barcode_scanner, scanner
        
        self.bar_signal.connect(self.set_value)
        self.video_signal.connect(self.setImage)
        
        barcode_scanner.start_listening("bar1", lambda x: self.bar_signal.emit(str(x, encoding='utf-8')))
        
        self.pushButton_product_up.clicked.connect(lambda: self.command_execute(f"MOVE 0 -{self.lineEdit_speedY.value() / 5.0} 0\r"))
        self.pushButton_product_down.clicked.connect(lambda: self.command_execute(f"MOVE 0 {self.lineEdit_speedY.value() / 5.0} 0\r"))
        self.pushButton_product_right.clicked.connect(lambda: self.command_execute(f"MOVE -{self.lineEdit_speedX.value() / 5.0} 0 0\r"))
        self.pushButton_product_left.clicked.connect(lambda: self.command_execute(f"MOVE {self.lineEdit_speedX.value() / 5.0} 0 0\r"))
        self.pushButton_up.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 -{self.lineEdit_speedZ.value() / 5.0}\r"))
        self.pushButton_down.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 {self.lineEdit_speedZ.value() / 5.0}\r"))
        
        self.pushButton_move_0.clicked.connect(lambda: self.command_execute("MOVE TO 0 0 0\r"))
        self.pushButton_move.clicked.connect(lambda: self.command_execute("MOVE TO {} {} {}\r".format(self.lineEdit_moveX.value() if self.radioButton_X.isChecked() else "0", 
                                                                                                       self.lineEdit_moveY.value() if self.radioButton_Y.isChecked() else "0",
                                                                                                       self.lineEdit_moveZ.value() if self.radioButton_Z.isChecked() else "0"
                                                                                                       )))
        
        self.pushButton_connection.clicked.connect(self.connect)
        
        self.pushButton_imageStop.clicked.connect(self.stop_stream)
        self.pushButton_imageDetect.clicked.connect(self.detect)
        self.pushButton_imageSave.clicked.connect(self.save_image)
        self.pushButton_load_trajectory.clicked.connect(self.get_traject_file)
        self.pushButton_trajectory_execute.clicked.connect(self.move_traject)
        self.pushButton_set_settings.clicked.connect(self.update_settings)
        
        self.pushButton_UpByZ.clicked.connect(lambda: self.Z_move(float(self.lineEdit_step_Z.value()), float(self.lineEdit_up_to_Z.text())))
        self.pushButton_downByZ.clicked.connect(lambda: self.Z_move(float(self.lineEdit_step_Z.value()), -float(self.lineEdit_down_to_Z.text())))
        
    def command_execute(self, command):
        global scanner
        
        if self.config["scanner_connected"]:
            self.listView_current_coordinate.addItem(f"[DEUBG] Send: {command}")
            response = scanner.send(command)
            self.listView_current_coordinate.addItem(f"[DEBUG] Response: {response[1]}")
        else:
            self.listView_current_coordinate.addItem(f"[DEBUG] No connection")
    
    
    def stop_stream(self):
        self.config["stream_stopped"] = not(self.config["stream_stopped"])
        self.pushButton_imageStop.setText("Старт" if self.config["stream_stopped"] else "Стоп")
        # if os.path.exists("temp.png"):
        #     os.remove("temp.png")
    
    
    def connect(self):
        global scanner, scanner_image
        
        # DEBUG
        # scanner.start_listening("get_image", lambda r: self.video_signal.emit(r[1]), "GET_IMAGE\r", 0)
        
        ip, port = self.lineEdit_ipScanner.text().split(":")
        (code, message) = scanner.connect(ip, int(port))
        (code1, message1) = scanner_image.connect(ip, int(port) + 1)
        if code == 0:
            self.config["scanner_connected"] = True
            self.listView_current_coordinate.addItem(f"[DEBUG] Successfully connected to [{ip}:{port}]")
            
            scanner.stop_listening()
            scanner.start_listening("get_status", lambda r: self.get_status(r), "GET_STATUS\r", 10)
            # scanner_image.start_listening("get_image", lambda r: self.video_signal.emit(r[1]), "GET_IMAGE\r", 0.8)
        else:
            self.listView_current_coordinate.addItem(f"[DEBUG] Failed to connect [{ip}:{port}]: {message}")


    def get_status(self, r):
        if r[0] == -1:
            self.connect()
            return
        data = json.loads(r[1].replace(b"OK GET_STATUS ", ""))
        self.lineEdit_currentZ.setText(data["position"]["z"])        
        print("[DEBUG] Status: OK")
    
    
    def Z_move(self, step, value):
        for i in range(float(self.lineEdit_currentZ.text()), value, step):
            self.command_execute(f"MOVE 0 0 {i}\r")
            if self.checkBox_save_z_stack.isChecked():
                self.save_image()
    
    
    def detect(self):
        global ie

        self.frame_large.pixmap().save("temp.png")
        image = cv2.cvtColor(cv2.imread("temp.png"), cv2.COLOR_BGR2RGB)
        preds = ie.predict("temp.png")
        for pred in preds:
            x1, y1, x2, y2 = int(pred[0]), int(pred[1]), int(pred[2]), int(pred[3])
            # cv2.putText(image, f"{pred[4]:.2%}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        height, width, channel = image.shape
        bytesPerLine = channel * width
        
        image = QtGui.QImage(image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        # image = convertToQtFormat.scaled(581, 371, QtCore.Qt.KeepAspectRatio)
        self.frame_large.setPixmap(QPixmap.fromImage(image))
        self.frame_large.adjustSize()
        os.remove("temp.png")
    
    
    def get_traject_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.csv *.txt)")
        self.config["traject_path"] = path[0]
        print(self.config["traject_path"], path[0])
    
    
    def move_traject(self):
        if os.path.exists(self.config["traject_path"]):
            with open(self.config["traject_path"], "r", encoding='utf-8') as fin:
                for line in fin:
                    try:
                        x, y, z = map(float, line[1:-2].split(','))
                        self.command_execute(f"MOVE {x} {y} {z}\r")
                        self.listView_current_coordinate.addItem(f"[DEBUG] MOVE {x} {y} {z}")
                    except Exception as e:
                        print("[DEBUG]", e)
        else:
            self.err_messsage("Файл {} не существует".format(self.config["traject_path"]))
    
    
    def update_settings(self):
        self.command_execute("SET_GAMMA {}\r".format(self.lineEdit_gamma.value()))
        self.command_execute("SET_BRIGHTNESS {}\r".format(self.lineEdit_brightness.value()))
        self.command_execute("SET_EXPOSURE_TIME {}\r".format(self.lineEdit_exposure_time.value()))
        self.command_execute("SET_CONTRAST {}\r".format(self.lineEdit_contrast.value()))
        
        
    def err_messsage(self, text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Ошибка")

        returnValue = msgBox.exec()
    
    
    def save_image(self):
        date = datetime.now()
        self.frame_large.pixmap().save(f"image_{self.lineEdit_scanerCode.text()}_{date.hour}_{date.minute}_{date.second}.png")
    
    
    @QtCore.pyqtSlot(str)
    def set_value(self, value):
        self.lineEdit_scanerCode.setText(value)
    
    
    @QtCore.pyqtSlot(bytes)
    def setImage(self, data):
        if not(self.config["stream_stopped"]):
            debug_data = data.split(b'\t')
            size = [int(x) for x in debug_data[0].decode().split('_')]
            print('[DEBUG]', size)
            data = debug_data[1]
            img = Image.frombytes('RGB', size, data)
            image = np.asarray(img)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            h, w, ch = image.shape
            bytesPerLine = ch * w
            image = QtGui.QImage(image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.frame_large.setPixmap(QPixmap.fromImage(image))
            self.frame_large.adjustSize()
    
    
    def close_event(self, event):
        global barcode_scanner, scanner
        barcode_scanner.stop_listening()
        scanner.stop_listening()


if __name__ == "__main__":
    global barcode_scanner, scanner, scanner_image, ie
    
    parser = argparse.ArgumentParser(prog='Web server application', usage='test.py [options]')
    parser.add_argument('--debug', type=bool, default=True, help='Run application in debug mode')
    parser.add_argument('--host', type=str, default="169.254.180.246", help='Host serialization')
    parser.add_argument('--port', type=int, default=5003, help='Port serialization')
    args = vars(parser.parse_args())
    
    scanner = Scanner(ip=args["host"], port=args["port"], debug=args["debug"])
    scanner_image = Scanner(ip=args["host"], port=args["port"] + 1, debug=args["debug"])
    barcode_scanner = Barcode_scanner(args["debug"])
    ie = Inference("model_v8l.pt")
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
