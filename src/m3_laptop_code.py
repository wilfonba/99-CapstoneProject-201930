"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Elijah Huff.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Elijah Huff")
    frame_label.grid(row=1, column=1)
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).
    arm_up_button = ttk.Button(frame, text='Arm up')
    speed_entry_box1 = ttk.Entry(frame, width=8)
    speed_entry_box1.insert(0, '100')
    speed_entry_box1.grid(row=2, column=2)
    arm_up_button.grid(row=2, column=1)

    arm_calibrate_button = ttk.Button(frame, text='Calibrate Arm')
    speed_entry_box2 = ttk.Entry(frame, width=8)
    speed_entry_box2.insert(0, '100')
    speed_entry_box2.grid(row=4, column=2)
    arm_calibrate_button.grid(row=4, column=1)

    arm_to_button = ttk.Button(frame, text='Arm to')
    speed_entry_box3 = ttk.Entry(frame, width=8)
    speed_entry_box3.insert(0, '100')
    position_entry_box = ttk.Entry(frame, width=8)
    position_entry_box.grid(row=5, column=3)
    speed_entry_box3.grid(row=5, column=2)
    arm_to_button.grid(row=5, column=1)

    arm_down_button = ttk.Button(frame, text='Arm down')
    speed_entry_box4 = ttk.Entry(frame, width=8)
    speed_entry_box4.insert(0, '100')
    speed_entry_box4.grid(row=3, column=2)
    arm_down_button.grid(row=3, column=1)

    go_until_color_button = ttk.Button(frame, text='Go until color')
    color_entry_box = ttk.Entry(frame, width=8)
    color_entry_box.grid(row=7, column=2)
    go_until_color_button.grid(row=7, column=3)

    speed_entry_label = ttk.Label(frame, text='Speed')
    speed_entry_label.grid(row=1, column=2)

    motor_position_label = ttk.Label(frame, text='Desired Motor Position (0 to 5112)')
    motor_position_label.grid(row=6, column=3)

    desired_colored_label = ttk.Label(frame, text='Stop At The Color:')
    desired_colored_label.grid(row=7, column=1)

    arm_up_button['command'] = lambda: handle_arm_up(speed_entry_box1, mqtt_sender)
    arm_calibrate_button['command'] = lambda: handle_calibrate_arm(speed_entry_box2, mqtt_sender)
    arm_to_button['command'] = lambda: handle_arm_to(speed_entry_box3, position_entry_box, mqtt_sender)
    arm_down_button['command'] = lambda: handle_arm_down(speed_entry_box4, mqtt_sender)
    go_until_color_button['command'] = lambda: handle_go_until_color(color_entry_box, mqtt_sender)
    # Return your frame:
    return frame


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
def handle_arm_up(speed_entry_box, mqtt_sender):
    print('Handle_arm_up: ', speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message('arm_up', [speed])


def handle_calibrate_arm(speed_entry_box, mqtt_sender):
    print('Handle_calibrate_arm: ', speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message('calibrate_arm', [speed])


def handle_arm_to(speed_entry_box, position_entry_box, mqtt_sender):
    print('Handle_arm_to: ', speed_entry_box.get())
    speed = int(speed_entry_box.get())
    position = int(position_entry_box.get())
    mqtt_sender.send_message('arm_to', [speed, position])


def handle_arm_down(speed_entry_box, mqtt_sender):
    print('Handle_arm_down: ', speed_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message('arm_down', [speed])


def handle_go_until_color(color_entry_box, mqtt_sender):
    print('Handle_go_until_color: ', color_entry_box.get())
    mqtt_sender.send_message('go_until_color', [color_entry_box.get()])

