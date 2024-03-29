from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import QtTest

from datetime import datetime
import numpy as np
import argparse
import threading
import logging
import sys, os
import json
import time
import cv2

from gui import Ui_MainWindow
from scanner import Scanner
from bscanner import Barcode_scanner
from inference import Inference
import config


logging.disable(logging.CRITICAL)


class VideoThread(QThread):
    signal = pyqtSignal(QImage)
    
    def __init__(self, ip, port):
        super(VideoThread, self).__init__()
        self.ip = ip
        self.port = port
        self.scanner = Scanner(ip=ip, port=port)
        self.stop = False

    def stop(self):
        self.stop = True
        
    def connect(self, ip, port):
        return self.scanner.connect(ip, port)

    def listener(self, data):
        try:
            if len(data) >= 0:
                # print("[IMAGE] len(data):", len(data))

                debug_data = data.split(config.delimiter)
                
                numbers = [float(x) for x in debug_data[0].decode().split('_')]
                coords = [numbers[2], numbers[3], numbers[4]]
                size = [int(numbers[0]), int(numbers[1])]
                # print("Motor status: moving {}, coords {}".format(size, coords))


                image = np.frombuffer(debug_data[1], dtype=np.uint32)
                image = image.view(np.uint8).reshape(tuple(size) + (-1,))

                bgr = image[..., :3]

                image = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
                image = cv2.rotate(image, cv2.ROTATE_180)
            
                h, w, ch = image.shape
                bytesPerLine = ch * w
                self.image = QImage(image.data, w, h, bytesPerLine, QImage.Format.Format_RGB888).copy()
                self.signal.emit(self.image)
        except Exception as e:
            print('[ERROR Video]', e)
        
    def run(self):
        self.stop = False
        while not(self.stop):
            try:
                code, data = self.scanner.send("GET_IMAGE\r", True)
                self.listener(data)
            except Exception as e:
                print(e)
            

class MainWindow(QMainWindow, Ui_MainWindow):
    bar_signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.config = {
            "stream_stopped": False,
            "bar_scanner": False,
            "scanner_connected": False,
            "video_stream": False,
            "image_received": False,
            "save_image": False,
            "save_path": "saved_data/"
        }
        
        self.initUi()
        self.set_listeners()
        
        
    def initUi(self):
        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)
        
        self.setupVideo()
    
    def set_listeners(self):
        global barcode_scanner, scanner
        
        self.connect(False)
        self.bar_signal.connect(self.set_value)
        
        # barcode_scanner.start_listening("bar1", lambda x: self.bar_signal.emit(str(x, encoding='utf-8')))
        
        self.button_move_left.clicked.connect(lambda: self.command_execute(f"MOVE 0 -{self.spinbox_stepY.value()} 0\r"))
        self.button_move_right.clicked.connect(lambda: self.command_execute(f"MOVE 0 {self.spinbox_stepY.value()} 0\r"))
        self.button_move_clockwise.clicked.connect(lambda: self.command_execute(f"MOVE -{self.spinbox_stepX.value()} 0 0\r"))
        self.button_move_counter_clockwise.clicked.connect(lambda: self.command_execute(f"MOVE {self.spinbox_stepX.value()} 0 0\r"))
        self.button_move_up.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 -{self.spinbox_stepZ.value()}\r"))
        self.button_move_down.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 {self.spinbox_stepZ.value()}\r"))
        
        self.button_connect.clicked.connect(self.connect)
        
        self.button_stop.clicked.connect(self.stop_stream)
        self.button_detect.clicked.connect(self.detect)
        self.button_save_image.clicked.connect(self.save_image)
        self.button_load_traject.clicked.connect(lambda: self.select_file('traject_path', "Image files (*.csv *.txt)", 'file', self.label_current_file))
        self.button_select_folder.clicked.connect(lambda: self.select_file('save_path', "Select Folder", 'folder', self.line_save_folder))
        self.button_start_traject.clicked.connect(self.move_traject)
        self.button_save_camera.clicked.connect(self.update_settings)
        
        self.button_move_up_Z.clicked.connect(lambda: self.command_execute(f"MOVE 0 0 -{self.spinbox_move_up_Z.value()}\r"))
        self.button_move_down_Z.clicked.connect(lambda: self.Z_move(self.spinbox_current_Z.value(), self.spinbox_move_down_Z.value(), self.spinbox_step.value()))
        self.autofocus_run.clicked.connect(self.autofocus)
            
    def command_execute(self, command, wait=False):
        global scanner
        
        if self.config["scanner_connected"]:
            self.listView_log.addItem(f"[DEUBG] Send: {command}")
            response = scanner.send(command, wait)
            if response[0] == 0:
                self.listView_log.addItem(f"[DEBUG] Response [{response[0]}]: {response[1]}")
                print(f"[DEBUG] Send: {command}")
                print(f"[DEBUG] Response: {response[1]}")
            else:
                self.config["scanner_connected"] = False
                scanner.shutdown()
                
                self.listView_log.addItem(f"[DEBUG] Disconnected")
                print(f"[DEBUG] Disconnected")
        else:
            self.listView_log.addItem(f"[DEBUG] No connection")
            print(f"[DEBUG] No connection")
    
    def connect(self, from_ui=True):
        global scanner
        
        (ip, port) = (None, None)
        (code1, message1) = (None, None)
        if from_ui:
            ip, port = self.line_scanner_ip.text().split(":")
            (code, message) = scanner.connect(ip, int(port))
            (code1, message1) = self.video_thread.connect(ip, int(port) + 1)
        else:
            ip, port = scanner.ip, int(scanner.port)
            self.line_scanner_ip.setText(f"{ip}:{port}")
            (code, message) = scanner.connect(ip, port)
            (code1, message1) = self.video_thread.connect(ip, port + 1)
            
        if (code == 0):# and (code1 == 0):
            self.config["scanner_connected"] = True
            self.listView_log.addItem(f"[DEBUG] Successfully connected to [{ip}:{port}]")
            
            scanner.stop_listening()
            print('video started')
            self.video_thread.start()
            # scanner.start_listening("get_status", lambda r: self.get_status(r), "GET_STATUS\r", 1)
            self.ratio_connect.click()
            # scanner.start_listening("get_gamma", lambda r: print("[GAMMA]", r), "GET_GAMMA\rGET_RESOLUTION\r", 9)
        else:
            self.config["scanner_connected"] = False
            self.listView_log.addItem(f"[DEBUG] Failed to connect [{ip}:{port}]: {message}")
            self.listView_log.addItem(f"[DEBUG] Failed to connect [{ip}:{port + 1}]: {message1}")
    
    def setupVideo(self):
        self.video_thread = VideoThread("", 0)
        self.video_thread.signal.connect(self.update_image)
        self.video_thread.start()
        
    @pyqtSlot(QImage)
    def update_image(self, image):
        if not(self.config["stream_stopped"]):
            try:
                self._img = QtGui.QImage(image).copy()
                self._pix = QtGui.QPixmap.fromImage(self._img)
                self.Frame.setPixmap(self._pix)
                QtGui.QGuiApplication.processEvents()
                if self.config["save_image"]:
                    self.save_image()
                    self.config["image_received"] = True
            except Exception as e:
                print('[GET_IMAGE]', e)
        
    def stop_stream(self):
        self.config["stream_stopped"] = not(self.config["stream_stopped"])
        self.button_stop.setText("Старт" if self.config["stream_stopped"] else "Остановить")
    
    def save_image(self):
        date = datetime.now()
        folder = self.config.get("save_path", "") if os.path.exists(self.config.get("save_path", "")) else ""
        path = f"{folder}image_{self.config.get('image_prefix', '')}_{self.line_qr.text()}_{date.hour:02d}_{date.minute:02d}_{date.second:02d}.png"
        print('save image:', path)
        self.Frame.pixmap().save(path)
    
    def wait_image(self):
        self.config["image_received"] = False
        self.config["save_image"] = True
        while not(self.config["image_received"]):
            QtTest.QTest.qWait(1)
    
    def get_status(self, r):
        try:
            rc, data = r
            if rc == -1:
                self.connect()
                return
            
            data = str(data, encoding='utf-8')
            if "coordinates" in data:
                data = json.loads(data)
                self.spinbox_current_Z.setValue(data["coordinates"]["z"])
                
                self.spinbox_currentX.setValue(data["coordinates"]["x"])
                self.spinbox_currentY.setValue(data["coordinates"]["y"])
                self.spinbox_currentZ.setValue(data["coordinates"]["z"])
            print("[STATUS]", r)
        except Exception as e:
            print('[STATUS]', e)

    def Z_move(self, start, end, step):
        def task():
            end2 = start - end
            self.wait_image()
            for i in np.arange(min(start, end2), max(start, end2), step):
                self.command_execute(f"MOVE 0 0 {step}\r")
                self.config["image_prefix"] = str(i + 1)
                self.wait_image()
            self.config["image_received"] = False
            self.config["save_image"] = False
        threading.Thread(target=task).run()
    
    
    def detect(self):
        global ie

        self.Frame.pixmap().save("temp.png")
        cv2.imwrite("temp.png", cv2.cvtColor(cv2.imread("temp.png"), cv2.COLOR_BGR2GRAY))
        image = cv2.cvtColor(cv2.imread("temp.png"), cv2.COLOR_BGR2RGB)
        preds = ie.predict("temp.png")
        print('DETECTED', preds)
        for pred in preds:
            x1, y1, x2, y2 = int(pred[0]), int(pred[1]), int(pred[2]), int(pred[3])
            # cv2.putText(image, f"{pred[4]:.2%}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        height, width, channel = image.shape
        bytesPerLine = channel * width
        
        image = QtGui.QImage(image.data, width, height, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
        self.Frame.setPixmap(QPixmap.fromImage(image))
        self.Frame.adjustSize()
#        os.remove("temp.png")
    
    
    def select_file(self, key, filter, type='file', label_out=None):
        if type == 'file':
            path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', filter=filter)[0]
        elif type == 'folder':
            path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.config[key] = path
        if label_out != None:
            label_out.setText(self.config[key])
        print(f"path: {self.config[key]}")
    
    
    def move_traject(self):
        if os.path.exists(self.config["traject_path"]):
            start = time.time()
            with open(self.config["traject_path"], "r", encoding='utf-8') as fin:
                for idx, line in enumerate(fin):
                    try:
                        x, y, z = map(float, line.split(','))
                        rc = self.command_execute(f"MOVE {x} {y} {z}\r", True)
                        print(1)
                        if self.checkBox.isChecked():
                            print(2)
                            self.config["image_prefix"] = str(idx + 1)
                            QtTest.QTest.qWait(5)
                            # QtTest.QTest.qWait((x + y + z) / 10)
                            self.wait_image()
                            self.save_image()
                    except Exception as e:
                        print(e)
            elapsed = time.time() - start
            logging.debug("Traject elapsed:", elapsed)
            self.spinbox_traject_time.setValue(elapsed)
        else:
            self.error_message("Файл {} не существует".format(self.config["traject_path"]))
        self.config["image_received"] = False
        self.config["save_image"] = False
    
    def autofocus(self):
        start = time.time()
        data = []
        start, end, step = 70, 100, 5
        rc = self.command_execute(f"MOVE 0 0 -150\r", True)
        #Fast
        rc = self.command_execute(f"MOVE 0 0 {start}\r", True)
        for z_pos in range(start, end + step, step):
            try:
                rc = self.command_execute(f"MOVE 0 0 {step}\r", True)
                self.wait_image()
                self.Frame.pixmap().save('tmp.png')
                image = cv2.imread('tmp.png')
                res = cv2.Laplacian(image, cv2.CV_64F).var()
                data.append((z_pos, res))
                print(f"Z [{z_pos}]: {res}")

            except Exception as e:
                print('[ERROR]', e)
        elapsed = time.time() - start
        mx = max(data, key=lambda x: x[1])
        rc = self.command_execute(f"MOVE 0 0 -{end - mx[0]}\r", True)
        print("Autofocus elapsed:", elapsed)
        print("Max:", mx)
        for i in data:
            print(i[0], i[1])
        self.config["image_received"] = False
        self.config["save_image"] = False

    def update_settings(self):
        self.command_execute("SET_GAMMA {}\r".format(int(self.spinbox_gamma.value())))
        self.command_execute("SET_BRIGHTNESS {}\r".format(int(self.spinbox_brightness.value())))
        self.command_execute("SET_EXPOSURE_TIME {}\r".format(int(self.spinbox_exposure_time.value())))
        self.command_execute("SET_CONTRAST {}\r".format(int(self.spinbox_contrast.value())))
        self.command_execute("SET_RESOLUTION {}\r".format(int(self.spindbox_resolution.value())))
        self.command_execute("SET_HUE {}\r".format(int(self.spinbox_hue.value())))
        self.command_execute("SET_TEMPERATURE_TINT {}\r".format(int(self.spinbox_imtemp.value())))
        
    def error_message(self, text):
        logging.error(text)
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Ошибка")
        msgBox.exec()
    
    @QtCore.pyqtSlot(str)
    def set_value(self, value):
        self.line_qr.setText(value)

    def closeEvent(self, event):
        os._exit(0)

if __name__ == "__main__":
    global barcode_scanner, scanner, ie
    parser = argparse.ArgumentParser(prog='Web server application', usage='test.py [options]')
    parser.add_argument('--debug', type=bool, default=True, help='Run application in debug mode')
    parser.add_argument('--host', type=str, default="192.168.1.118", help='Host serialization')
    parser.add_argument('--port', type=int, default=6003, help='Port serialization')
    args = vars(parser.parse_args())
    
    scanner = Scanner(ip=args["host"], port=args["port"])
    barcode_scanner = Barcode_scanner()
    ie = Inference("data/model_v8l.pt")
    
    logging.basicConfig(level=logging.DEBUG)

    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(lambda: os._exit(0))
    window = MainWindow()
    window.show()
    app.exec()
