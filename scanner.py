
import threading
import socket
import logging
import time

import config

class Scanner:
    
    def __init__(self, protocol, ip=None, port=None, dst_ip=None, dst_port=None):
        self.listeners = {}
        self.stop = False
        self.protocol = protocol
        self.ip = ip
        self.port = port
        self.recv_ip = dst_ip
        self.recv_port = dst_port
        self.status = False
        try:
            if self.protocol == 'TCP':
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.data = b''
            elif self.protocol == 'UDP':
                self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                self.sock.bind((self.ip, self.port))
            else:
                raise ValueError
            self.status = True
        except Exception as e:
            logging.error("Connection error:", e)
            raise ConnectionError
    
    
    def shutdown(self):
        self.status = False
        self.sock.close()
        self.sock.shutdown(socket.SHUT_RDWR)
    
    
    def reconnect(self):
        self.shutdown()
        self.connect(self.ip, self.port)
        
        
    def connect(self, ip, port):
        try:
            self.recv_ip = ip
            self.recv_port = port
            if self.protocol == 'TCP':
                self.sock.connect((ip, port))
            elif self.protocol == 'UDP':
                pass
            self.status = True
            return (0, "OK")
        except Exception as e:
            return (-1, e)
    
        
    def send(self, message, wait=False):
        try:
            if self.protocol == 'TCP':
                self.sock.send(bytes(message, encoding='utf-8'))
                if wait:
                    data = ''
                    while data == '':
                        data = self.recvall()
                    logging.debug(f"Received {len(data)} bytes")
                return (0, data)
            elif self.protocol == 'UDP':
                self.sock.sendto(bytes(message, encoding='utf-8'), (self.recv_ip, self.recv_port))
            return (0, "")
        except Exception as e:
            self.stop_listening()
            self.reconnect()
            return (-1, e)
    
    
    def recvall(self):
        buffer = ''
        while (self.data.find(config.start_bytes) == -1) or (self.data.find(config.end_bytes) == -1) and not (self.data.find(config.end_bytes) > self.data.find(config.start_bytes)):
            if self.protocol == 'TCP':
                buffer = self.sock.recv()
            elif self.protocol == 'UDP':
                buffer, addr = self.sock.recvfrom(65527)
            self.data += buffer
        start_pos = self.data.find(config.start_bytes) + len(config.start_bytes)
        stop_pos = self.data.find(config.end_bytes)
        data_to_return = self.data[start_pos:stop_pos].replace(config.start_bytes, '').replace(config.end_bytes, '')
        self.data = self.data[stop_pos + len(config.end_bytes):]
        return data_to_return


    def start_listening(self, name, listener, command, sleep):
        self.stop = False
        self.listeners[name] = threading.Thread(target=self.listen, args=(listener, command, sleep))
        self.listeners[name].start()
    
    
    def stop_listening(self):
        self.stop = True
    
    
    def listen(self, listener, command, sleep=1):
        logging.debug(f"Start listening scanner {self.ip}:{self.port}")
        while not(self.stop) or not(self.status):
            code, data = self.send(command, True)
            listener((code, data))
            logging.debug(f"[DEBUG] Scanner [{self.ip}]: {code}")
            time.sleep(sleep)
