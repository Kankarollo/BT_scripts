import subprocess
import logging
import threading
import time

class BluetoothCTL():
    """Class for using bluetoothctl module from python."""

    def __init__(self,command="bluetoothctl":str):
        logging.basicConfig(level=logging.INFO, format='[%(levelname)s]: %(message)s')
        self.logger = logging.getLogger("bluetooth")
        self.ps = subprocess.Popen([command], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
        universal_newlines=True)
        self.output = ""
        
    def start_listening(self):
        """Start threads that is listening and printing stdout of a process."""

        self.t1 = threading.Thread(target=self.read_from_process)
        self.t1.start()

    def read_from_process(self):
        """Printing stdout of a process. Executed from threads to avoid deadlock."""

        while self.ps.poll() == None:
            self.output = self.ps.stdout.readline()
            print(self.output,end="")

    def write_to_process(self,input:str):
        """Writing commands to a process by stdin.
        
        Args:
            input(str): String to be send to the process by stdin.
        
        """

        self.ps.stdin.write(input + "\n")
        self.ps.stdin.flush()

    def stop(self):
        """Stop process."""

        if self.ps.poll() == None:
            self.ps.kill()
            self.logger.info("Killing process")

    def execute_command(self, command:str):
        """Execute command by sending it to process by stdin and wait for response.
        
        Args:
            command(str): Command to be executed by the bluetoothctl.
        
        """

        time_last_msg = time.time()
        last_msg = ""
        self.write_to_process(command)
        while self.ps.poll() == None:
            if self.output != last_msg:
                last_msg = self.output
                time_last_msg = time.time()
            else:
                if (time.time() - time_last_msg) > 3.0:
                    break
    
    def look_for_available_devices(self,devices_addr:list):
        """Use command 'scan on' to look for given devices.
        
        Args:
            devices_addr(list(str)): List of mac addresses to be searched for.
        
        Returns:
            founded_devices: List of founded mac addresses.
        """

        founded_devices = []
        self.write_to_process("scan on")
        time_last_msg = time.time()
        last_msg = ""
        while self.ps.poll() == None:
            if self.output != last_msg:
                last_msg = self.output
                for address in devices_addr:
                    if address in last_msg:
                        founded_devices.append(address)
                time_last_msg = time.time()
            else:
                if (time.time() - time_last_msg) > 3.0:
                    break
        return founded_devices