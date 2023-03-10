from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from datetime import datetime
from PIL import Image
import numpy as np
import argparse
import logging
import sys, os
import json
import time
import cv2

# from gui import Ui_MainWindow
from test import Ui_MainWindow
from utils import Scanner, Barcode_scanner
from inference import Inference


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    bar_signal = QtCore.pyqtSignal(str)
    video_signal = QtCore.pyqtSignal(bytes)
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.config = {
            "stream_stopped": False,
            "bar_scanner": False,
            "scanner_connected": False,
            "video_stream": False,
            "speed_x": 1
        }
        
        self.initUi()
        self.set_listeners()
        
        
        
    def initUi(self):
        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
    def set_listeners(self):
        global barcode_scanner, scanner
        
        self.connect(False)
        self.bar_signal.connect(self.set_value)
        self.video_signal.connect(self.setImage)
        
        barcode_scanner.start_listening("bar1", lambda x: self.bar_signal.emit(str(x, encoding='utf-8')))
        
        self.button_move_left.clicked.connect(lambda: self.command_execute(f"MOVE 0 -{self.spinbox_stepY.value()} 0\r"))
        self.button_move_right.clicked.connect(lambda: self.command_execute(f"MOVE 0 {self.spinbox_stepY.value()} 0\r"))
        self.button_move_clockwise.clicked.connect(lambda: self.command_execute(f"MOVE -{self.spinbox_stepX.value()} 0 0\r"))
        self.button_move_counter_clockwise.clicked.connect(lambda: self.command_execute(f"MOVE {self.spinbox_stepX.value()} 0 0\r"))
        self.button_move_up.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 -{self.spinbox_stepZ.value()}\r"))
        self.button_move_down.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 {self.spinbox_stepZ.value()}\r"))
        
        # self.pushButton_move_0.clicked.connect(lambda: self.command_execute("MOVE TO 0 0 0\r"))
        # self.pushButton_move.clicked.connect(lambda: self.command_execute("MOVE TO {} {} {}\r".format(self.lineEdit_moveX.value() if self.radioButton_X.isChecked() else "0", 
        #                                                                                                self.lineEdit_moveY.value() if self.radioButton_Y.isChecked() else "0",
        #                                                                                                self.lineEdit_moveZ.value() if self.radioButton_Z.isChecked() else "0"
        #                                                                                                )))
        
        self.button_connect.clicked.connect(self.connect)
        
        self.button_stop.clicked.connect(self.stop_stream)
        self.button_detect.clicked.connect(self.detect)
        self.button_save_image.clicked.connect(self.save_image)
        self.button_load_traject.clicked.connect(self.get_traject_file)
        self.button_start_traject.clicked.connect(self.move_traject)
        self.button_save_camera.clicked.connect(self.update_settings)
        
        self.button_move_up_Z.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 -{self.spinbox_move_up_Z.value()}\r"))
        self.button_move_down_Z.clicked.connect(lambda: self.Z_move(self.spinbox_step.value(), self.spinbox_move_down_Z.text()))
        
        
    def command_execute(self, command):
        global scanner, logger
        logger.debug(f"[DEUBG] Try: {command}")
        if self.config["scanner_connected"]:
            self.listView_log.addItem(f"[DEUBG] Send: {command}")
            response = scanner.send(command)
            self.listView_log.addItem(f"[DEBUG] Response: {response[1]}")
            logger.debug(f"[DEUBG] Send: {command}")
            logger.debug(f"[DEBUG] Response: {response[1]}")
        else:
            self.listView_log.addItem(f"[DEBUG] No connection")
            logger.debug(f"[DEBUG] No connection")
    
    
    def stop_stream(self):
        self.config["stream_stopped"] = not(self.config["stream_stopped"])
        self.button_stop.setText("Старт" if self.config["stream_stopped"] else "Остановить")
    
    
    def connect(self, from_ui=True):
        global scanner, scanner_image, logger
        
        (ip, port) = (None, None)
        (code1, message1) = (None, None)
        if from_ui:
            ip, port = self.line_scanner_ip.text().split(":")
            (code, message) = scanner.connect(ip, int(port))
            (code1, message1) = scanner_image.connect(ip, int(port) + 1)
        else:
            ip, port = scanner.ip, int(scanner.port)
            self.line_scanner_ip.setText(f"{ip}:{port}")
            (code, message) = scanner.connect(ip, port)
            (code1, message1) = scanner_image.connect(ip, port + 1)
            
        if (code == 0) and (code1 == 0):
            self.config["scanner_connected"] = True
            self.listView_log.addItem(f"[DEBUG] Successfully connected to [{ip}:{port}]")
            
            scanner.stop_listening()
            scanner.start_listening("get_status", lambda r: self.get_status(r), "GET_STATUS\r", 10)
            scanner_image.start_listening("get_image", lambda r: self.video_signal.emit(r[1]), "GET_IMAGE\r", 0)
        else:
            self.listView_log.addItem(f"[DEBUG] Failed to connect [{ip}:{port}]: {message}")
            self.listView_log.addItem(f"[DEBUG] Failed to connect [{ip}:{port + 1}]: {message1}")


    def get_status(self, r):
        global logger
        
        if r[0] == -1:
            self.connect()
            return
        data = str(r[1], encoding='utf-8')
        if "coordinates" in data:
            data = json.loads(data)
            self.spinbox_current_Z.setValue(data["coordinates"]["z"])        
        logger.debug("Status: OK")
    
    
    def Z_move(self, step, value):
        start = int(float(str(self.spinbox_current_Z.value()).replace(',', '.')))
        end = int(float(str(value).replace(',', '.')))
        step = int(float(str(step).replace(',', '.')))
        for i in range(start, end, step * (step // abs(step))):
            self.command_execute(f"MOVE 0 0 {step}\r")
            time.sleep(1)
            if self.checkBox_save.isChecked():
               self.save_image()
            
    
    
    def detect(self):
        global ie

        self.Frame.pixmap().save("temp.png")
        image = cv2.cvtColor(cv2.imread("temp.png"), cv2.COLOR_BGR2RGB)
        preds = ie.predict("temp.png")
        for pred in preds:
            x1, y1, x2, y2 = int(pred[0]), int(pred[1]), int(pred[2]), int(pred[3])
            # cv2.putText(image, f"{pred[4]:.2%}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        height, width, channel = image.shape
        bytesPerLine = channel * width
        
        image = QtGui.QImage(image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.Frame.setPixmap(QPixmap.fromImage(image))
        self.Frame.adjustSize()
        os.remove("temp.png")
    
    
    def get_traject_file(self):
        global logger
        
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', filter="Image files (*.csv *.txt)")
        self.config["traject_path"] = path[0]
        logger.debug(f"{self.config['traject_path']} {path[0]}")
    
    
    def move_traject(self):
        global logger
        
        if os.path.exists(self.config["traject_path"]):
            with open(self.config["traject_path"], "r", encoding='utf-8') as fin:
                for line in fin:
                    try:
                        x, y, z = map(float, line.split(','))
                        self.command_execute(f"MOVE {x} {y} {z}\r")
                        time.sleep(3)
                    except Exception as e:
                        logger.debug(e)
        else:
            self.error_message("Файл {} не существует".format(self.config["traject_path"]))
    
    
    def update_settings(self):
        self.command_execute("SET_GAMMA {}\r".format(self.spinbox_gamma.value()))
        self.command_execute("SET_BRIGHTNESS {}\r".format(self.spinbox_brightness.value()))
        self.command_execute("SET_EXPOSURE_TIME {}\r".format(self.spinbox_exposure_time.value()))
        self.command_execute("SET_CONTRAST {}\r".format(self.spinbox_contrast.value()))
        
        
    def error_message(self, text):
        global logger
        logger.error(text)
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Ошибка")

        returnValue = msgBox.exec()
    
    
    def save_image(self):
        date = datetime.now()
        path = self.line_save_folder.text() if os.path.exists(self.line_save_folder.text()) else ""
        self.Frame.pixmap().save(f"{path}/image_{self.line_qr.text()}_{date.hour}_{date.minute}_{date.second}.png")
    
    
    @QtCore.pyqtSlot(str)
    def set_value(self, value):
        self.line_qr.setText(value)
    
    
    @QtCore.pyqtSlot(bytes)
    def setImage(self, data):
        global logger
        
        if not(self.config["stream_stopped"]):
            debug_data = data.split(b'\t')
            size = [int(x) for x in debug_data[0].decode().split('_')]
            logger.debug(f"Image size: {size}")
            data = debug_data[1]
            img = Image.frombytes('RGB', size, data)
            image = np.asarray(img)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            h, w, ch = image.shape
            bytesPerLine = ch * w
            image = QtGui.QImage(image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.Frame.setPixmap(QPixmap.fromImage(image))
            self.Frame.adjustSize()


if __name__ == "__main__":
    global barcode_scanner, scanner, scanner_image, ie, logger
    
    parser = argparse.ArgumentParser(prog='Web server application', usage='test.py [options]')
    parser.add_argument('--debug', type=bool, default=True, help='Run application in debug mode')
    parser.add_argument('--host', type=str, default="169.254.180.246", help='Host serialization')
    parser.add_argument('--port', type=int, default=6003, help='Port serialization')
    args = vars(parser.parse_args())
    
    scanner = Scanner(ip=args["host"], port=args["port"])
    scanner_image = Scanner(ip=args["host"], port=args["port"] + 1)
    barcode_scanner = Barcode_scanner()
    ie = Inference("model_v8l.pt")
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.error("Test")
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
