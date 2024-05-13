import serial
import time

#Setup the serial connection
ser = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate as necessary
time.sleep(2)  # Allow time for the connection to establish

def send_command(command):
    print("Sending command:", command)  # Printing command to console for debug
    ser.write((command + '\n').encode())

def move_arm(base, shoulder, elbow, wrist, wristRotate, gripper):
    command = f"MOVE,{base},{shoulder},{elbow},{wrist},{wristRotate},{gripper}"
    send_command(command)

def interpolate_move(start, end, steps=10):
    # Generate steps linearly between start and end positions
    for step in range(1, steps + 1):
        interpolated_position = [
            int(start[i] + (end[i] - start[i]) * step / steps) for i in range(len(start))
        ]
        move_arm(*interpolated_position)
        time.sleep(0.1)  # Control speed of interpolation

def move_step_by_step():
    commands = [
        (60, 90, 130, 150, 90, 70),
        (68, 90, 130, 150, 90, 70),
        (66, 90, 147, 150, 90, 70),
        (66, 90, 147, 140, 90, 70),
        (66, 90, 147, 140, 80, 120),
        (66, 90, 130, 140, 80, 120),
        (90, 90, 130, 140, 80, 120),
        (90, 90, 140, 140, 80, 120),
        (90, 90, 140, 140, 80, 70),
        (60, 90, 130, 150, 90, 70),
        (50, 90, 130, 150, 90, 70),
        (50, 90, 130, 130, 90, 70),
        (50, 90, 152, 130, 80, 70),
        (50, 90, 152, 130, 80, 120),
        (50, 90, 130, 130, 80, 120),
        (66, 90, 130, 130, 80, 120),
        (66, 90, 147, 130, 80, 120),
        (66, 90, 147, 137, 80, 120),
        (66, 90, 147, 137, 80, 70),
        (60, 90, 130, 150, 90, 70)
    ]
    for i in range(len(commands) - 1):
        interpolate_move(commands[i], commands[i+1])
        time.sleep(1)  # Optional: add extra delay between major movements

#Run the step-by-step movement
move_step_by_step()