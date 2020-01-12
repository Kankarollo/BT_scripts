#!/usr/bin/python3

import subprocess
from time import sleep
import logging

def write_to_process(proc,input):
    proc.stdin.write(input + "\n")
    proc.stdin.flush()

def main():
    ps = subprocess.Popen(("bluetoothctl"), stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
    write_to_process(ps,f"scan on")
    logging.info(f"Scanning...")
    sleep(5)
    for mac_addr in mac_address:
        write_to_process(ps,f"pair {mac_addr}")
        logging.info(f"Pairing to {mac_addr}...")
        sleep(7)
        write_to_process(ps,f"connect {mac_addr}")
        logging.info(f"Connecting to {mac_addr}...")
        sleep(7)
    write_to_process(ps,'.')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s]: %(message)s")
    mac_address = [""]
    main()
