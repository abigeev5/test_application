import socket, serial
import time, glob, sys
import threading
import logging

import config

class Barcode_scanner:
    
    def __init__(self):
        self.ports = self.serial_ports(9600)
        self.stop = False
        self.listeners = {}
        if len(self.ports) > 0:
            try:
                self.ser = serial.Serial(self.ports[0], 9600)
                logging.debug(f"Serial: {self.ser}")
            except Exception as e:
                logging.error(f"Cant serialize com port [{self.ports[0]}]: {e}")
        else:
            logging.debug("No COM ports to listen")

    
    def listen(self, listener):
        if len(self.ports) > 0:
            logging.debug(f"Start listening {self.ports[0]}")
            buffer = b""
            while not(self.stop):
                data = self.ser.read()
                if data == b"\r":
                    listener(buffer)
                    buffer = b""
                elif data != b"":
                    buffer += data
        else:
            logging.debug(f"[DEBUG] No COM ports to listen")
    
    
    def start_listening(self, name, listener):
        self.listeners[name] = threading.Thread(target=self.listen, args=(listener, ))
        self.listeners[name].start()
    
    
    def stop_listening(self):
        self.stop = True
        # if name in self.listeners:
        #     self.listeners[name].stop()
    
                
    def serial_ports(self, bandurate=9600):
        if sys.platform.startswith('win'):
            ports = [f'COM{i}' for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port, baudrate=bandurate)
                s.close()
                result.append(port)
            except Exception:
                pass
        return result