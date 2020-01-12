#!/usr/bin/python3

from BluetoothCtl import BluetoothCTL

def main():
    device_mac_addr = [""]
    bluetoothctl = BluetoothCTL("bluetoothctl")
    bluetoothctl.start_listening()
    for device in device_mac_addr:
        bluetoothctl.execute_command(f"remove {device}")
    bluetoothctl.stop()

if __name__ == "__main__":
    main()