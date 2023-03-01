import socket, serial
import sys
import threading
import time

class Scanner:
    def __init__(self, ip=None, port=None, debug=False):
        self.debug = debug
        self.listeners = {}
        self.stop = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self, ip, port):
        try:
            self.sock.connect((ip, port))
            self.ip = ip
            self.port = port
            return (0, "OK")
        except Exception as e:
            # DEBUG
            self.ip = None
            self.port = None
            return (-1, e)
        
    def send(self, message, wait=False):
        #if self.debug:
            # print(message)
            #if message == "GET_IMAGE\r":
                #return (0, cv2.imencode('.bmp', cv2.imread("test.bmp"))[1].tobytes())
                #return (0, cv2.imread("test.bmp"))
        self.sock.send(bytes(message, encoding='utf-8'))
        if wait:
            # conn, addr = self.revicer.accept()
            data = self.recvall(4096 * 32)
            # data = data.decode('utf-8')
            # conn.close()
            print(len(data))
            return (0, data)
            if self.debug:
                print(f"[DEBUG] From hz: {data}")
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
        while True:
            part = self.sock.recv(buffer)
            data += part
            if len(part) < buffer:
                break
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
        if self.debug:
            # print(f"[DEBUG] Start listening scanner {self.ip}:{self.port}")
            pass
        while True:
            if self.stop:
                break
            code, data = self.send(command, True)
            listener((code, data))
            if self.debug:
                # print(f"[DEBUG] Scanner [{self.ip}]: {code}, {data}")
                pass
            time.sleep(sleep)


class Barcode_scanner:
    def __init__(self, debug=False):
        self.ports = self.serial_ports(9600)
        self.debug = debug
        self.stop = False
        self.listeners = {}
        try:
            self.ser = serial.Serial(self.ports[0], 9600)
            if self.debug:
                print("[DEBUG] Serial:", self.ser)
        except Exception as e:
            print("[ERROR] Cant serialize com port")

    
    def listen(self, listener):
        if len(self.ports) > 0:
            if self.debug:
                print(f"[DEBUG] Start listening {self.ports[0]}")
            buffer = b""
            while True:
                if self.stop:
                    break
                data = self.ser.read()
                if data == b"\r":
                    listener(buffer)
                    buffer = b""
                elif data != b"":
                    buffer += data
        else:
            if self.debug:
                print(f"[DEBUG] No COM ports to listen")
    
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