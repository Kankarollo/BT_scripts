#!/usr/bin/python3

from BluetoothCtl import BluetoothCTL   

def main():
    founded_devices = []
    device_mac_addr = [""]
    bluetoothctl = BluetoothCTL("bluetoothctl")
    bluetoothctl.start_listening()
    founded_devices = bluetoothctl.look_for_available_devices(device_mac_addr)
    for device in founded_devices:
        bluetoothctl.execute_command(f"pair {device}")
        bluetoothctl.execute_command(f"connect {device}")

    bluetoothctl.stop()

if __name__ == "__main__":
    main()