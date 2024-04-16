import serial
import time

#The locations need to be ready first .

class arm:
    def __init__(self, port):
        self.connection = serial.Serial(port, 9600, timeout=1)
        # Wait for the connection to establish
        time.sleep(2)

    def move_to_position(self, position):
        
        self.send_command(f"MOVE {position}\n")

    def close(self):

        self.connection.close()

    def drop(self) -> None:
        self.command(192)
    
    def grasp(self) -> None:
        self.command("g")

    
