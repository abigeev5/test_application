import socket, serial
import time, glob, sys
import threading
import logging

class Scanner:
    
    def __init__(self, ip=None, port=None):
        self.listeners = {}
        self.stop = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
    
        
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
            # conn, addr = self.revicer.accept()
            data = self.recvall(4096 * 32)
            logging.debug(f"Recived {len(data)} bytes")
            return (0, data)
            if data is None:
                return (-1, data)
            else:
                if "FAIL" in data:
                    return (1, data)
                elif "OK" in data:
                    return (0, data)
                return (2, data)
        else:
            return (0, "")
    
    
    def recvall(self, buffer=4096):
        data = b""
        part = '0' * buffer
        while len(part) >= buffer:
            part = self.sock.recv(buffer)
            data += part
        return data


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
            logging.debug(f"[DEBUG] Scanner [{self.ip}]: {code}, {data}")
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