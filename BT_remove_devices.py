#!/usr/bin/python3

import subprocess
import logging

def read_from_process(proc):
    while True:
        line = proc.stdout.readline()
        if "Invalid command" in line:
            break
        if "has been removed" in line:
            logging.info(line)
        if "not available" in line:
            logging.info(line)


def write_to_process(proc,input):
    proc.stdin.write(input + "\n")
    proc.stdin.flush()

def main():
    ps = subprocess.Popen(("bluetoothctl"), stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
    for mac_addr in mac_address:
        write_to_process(ps,f"remove {mac_addr}")
    write_to_process(ps,'.')
    read_from_process(ps)

if __name__ == "__main__":
    logging.basicConfig(filename="file.log",filemode='a+',level=logging.INFO, format='%(asctime)s %(message)s')
    # logger = logging.getLogger("Bluetooth remove logger")
    logging.info("BT_remove_device executing...")
    mac_address = [""]
    main()
    logging.info("Completed succesfully")