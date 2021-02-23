import os
import sys
import time
import serial
import datetime
import threading

# Reference: https://gist.github.com/RoganDawes/1042a316a9d320d5e2ff


def open_and_read_serial_forever(serial_port, baudrate, node_name):
    this_serial = serial.Serial(serial_port, baudrate, timeout=0)
    this_serial.bytesize = serial.EIGHTBITS         # number of bits per bytes
    this_serial.parity = serial.PARITY_NONE         # set parity check: no parity
    this_serial.stopbits = serial.STOPBITS_ONE      # number of stop bits
    this_serial.timeout = 0                         # non blocking read
    this_serial.xonxoff = False                     # disable software flow control
    this_serial.rtscts = False                      # disable hardware (RTS/CTS) flow control
    this_serial.dsrdtr = False                      # disable hardware (DSR/DTR) flow control
    this_serial.writeTimeout = 2                    # timeout for write
    this_logfile = node_name + ".txt"
    # if os.path.exists(self.logfile):
    #    os.remove(self.logfile)
    # lock to serialize console output
    this_lock = threading.Lock()
    # try:
    #     this_serial.open()
    # except Exception as e:
    #     print("[ERROR] Can't open serial port [{}]: ".format(serial_port) + str(e))
    #     exit()
    if this_serial.isOpen():
        try:
            while True:
                # c = this_serial.read(size=1024)
                data = this_serial.readline().decode('ascii').rstrip('\r\n')
                with this_lock:
                    if data:
                        with open(this_logfile, 'a') as logfile:
                            string_to_log = node_name + " @ " + str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")) + " -> " + data + "\n"
                            print(string_to_log, end="")
                            logfile.write(string_to_log)
        except Exception as e1:
            print("[ERROR] With Communication: " + str(e1))
    else:
        print("[ERROR] Can't open serial port: ")
        exit()
    pass

#
# def log(self):
#     data = this_serial.readline().decode('ascii').rstrip('\r\n')
#     if data:
#         with open(self.logfile, 'a') as logfile:
#             string_to_log = str(datetime.datetime.now()) + " ::::: " + data + '\n'
#             print(string_to_log, end='')
#             logfile.write(string_to_log)
#         pass
#     pass

