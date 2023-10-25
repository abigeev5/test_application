
import threading
import socket
import logging
import time

import config

class Scanner:
    
    def __init__(self, ip=None, port=None):
        self.listeners = {}
        self.stop = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
    
    
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
        print("Message send:", len(message), message)
        self.sock.send(bytes(message, encoding='utf-8'))
        if wait:
            try:
                data = self.recvall(4 * 1024 * 1024)
                print(f"Received {len(data)} bytes")
                return (0, data)
            except Exception as e:
                print("Error", e)
                return (0, "")
        else:
            return (0, "")
    
    
    def recvall(self, package_size=4096):
        try:
            self.data = b''
            buffer = '0' * package_size
            while (self.data.find(config.start_bytes) == -1) or (self.data.find(config.end_bytes) == -1):
                buffer = self.sock.recv(package_size)
                self.data += buffer
#                print('[DATA]', len(self.data))
            start_pos = self.data.find(config.start_bytes) + len(config.start_bytes)
            stop_pos = self.data.find(config.end_bytes)
            data_to_return = self.data[start_pos:stop_pos]
            print(f'[DEBUG] bytes: {len(data_to_return)} start_pos: {start_pos} end_pos: {stop_pos}')
#            self.data = self.data[stop_pos + len(config.end_bytes):]
            return data_to_return
        except Exception as e:
            print("Error", e)
            return (0, "")


    def start_listening(self, name, listener, command, sleep):
        self.stop = False
        self.listeners[name] = threading.Thread(target=self.listen, args=(listener, command, sleep))
        self.listeners[name].start()
    
    
    def stop_listening(self):
        self.stop = True
        # if name in self.listeners:
        #    self.listeners[name].stop()
    
    
    def listen(self, listener, command, sleep=10):
        try:
            logging.debug(f"Start listening scanner {self.ip}:{self.port}")
            while not(self.stop):
                code, data = self.send(command, True)
                listener((code, data))
                logging.debug(f"[DEBUG] Scanner [{self.ip}]: {code}")
                time.sleep(sleep)
        except Exception as e:
            print("Error", e)
            return (0, "")
