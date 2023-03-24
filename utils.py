import socket, serial
import time, glob, sys
import threading
import logging

import config
class Scanner:
    
    def __init__(self, ip=None, port=None):
        self.listeners = {}
        self.stop = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.data = b''
    
    
    def shutdown(self):
        self.sock.shutdown(socket.SHUT_RDWR)
    
    
    def reconnect(self):
        self.shutdown()
        self.connect(self.ip, self.port)
    
        
    def connect(self, ip, port):
        try:
            self.sock.connect((ip, port))
            self.ip = ip
            self.port = port
            return (0, "OK")
        except Exception as e:
            return (-1, e)
    
        
    def send(self, message, wait=False):
        self.sock.send(bytes(message, encoding='utf-8'))
        if wait:
            data = self.recvall(4096 * 32)
            logging.debug(f"Received {len(data)} bytes")
            return (0, data)
        else:
            return (0, "")
    
    
    def recvall(self, package_size=4096):
        buffer = '0' * package_size
        while (self.data.find(config.start_bytes) == -1) or (self.data.find(config.end_bytes) == -1) and not (self.data.find(config.end_bytes) > self.data.find(config.start_bytes)):
            buffer = self.sock.recv(package_size)
            self.data += buffer
        start_pos = self.data.find(config.start_bytes) + len(config.start_bytes)
        stop_pos = self.data.find(config.end_bytes)
        data_to_return = self.data[start_pos:stop_pos]
        self.data = self.data[stop_pos + len(config.end_bytes):]
        return data_to_return


    def start_listening(self, name, listener, command, sleep):
        self.stop = False
        self.listeners[name] = threading.Thread(target=self.listen, args=(listener, command, sleep))
        self.listeners[name].start()
    
    
    def stop_listening(self):
        self.stop = True
        # if name in self.listeners:
        #    self.listeners[name].stop()
    
    
    def listen(self, listener, command, sleep=10):
        logging.debug("Start listening scanner {self.ip}:{self.port}")
        while not(self.stop):
            code, data = self.send(command, True)
            listener((code, data))
            logging.debug(f"[DEBUG] Scanner [{self.ip}]: {code}")
            time.sleep(sleep)


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