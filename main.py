import sys
import threading
from SERIAL_COMM import open_and_read_serial_forever


def main():
    serial_port_to_node = {"COM11": "Node-1", "COM19": "Node-2", "COM20": "Node-3"}
    # Create two threads as follows
    try:
        for serial_port, node in serial_port_to_node.items():
            t = threading.Thread(target=open_and_read_serial_forever, args=(serial_port, 115200, node))
            t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
            t.start()
    except:
        print("Error: unable to start thread")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        exit()
    pass


if __name__ == "__main__":
    main()

