#!/usr/bin/python3

import subprocess
from time import sleep

def write_to_process(proc,input):
    proc.stdin.write(input + "\n")
    proc.stdin.flush()

def main():
    ps = subprocess.Popen(("bluetoothctl"), stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
    write_to_process(ps,f"scan on")
    print(f"Scanning...")
    sleep(2)
    for mac_addr in mac_address:
        write_to_process(ps,f"pair {mac_addr}")
        print(f"Pairing to {mac_addr}...")
        sleep(5)
        write_to_process(ps,f"connect {mac_addr}")
        print(f"Connecting to {mac_addr}...")
        sleep(5)
    write_to_process(ps,'.')

if __name__ == "__main__":
    mac_address = [""]
    main()
