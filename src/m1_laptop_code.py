"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Maddie Sorensen.
  Spring term, 2018-2019.
"""
# Done:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Maddie Sorensen")
    frame_label.grid(row=0,column=2)
    # Done: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).




    entry_distance=ttk.Entry(frame, width=8)
    entry_distance.insert(0,"100")
    entry_distance_label= ttk.Label(frame, text="Distance")
    entry_distance_label.grid(row=2, column=2)
    entry_distance.grid(row=3, column=2)

    entry_speed = ttk.Entry(frame, width=8)
    entry_speed.insert(0, "100")
    entry_speed.grid(row=5, column=2)
    entry_speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    entry_speed_label.grid(row=4, column=2)

    forward_button = ttk.Button(frame, text="Move Forward")
    forward_button.grid(row=1, column=0)
    forward_button['command'] = lambda: handle_move_forward(entry_speed, entry_distance, mqtt_sender)

    backward_button = ttk.Button(frame, text="Move Backward")
    backward_button.grid(row=1, column=3)
    backward_button['command'] = lambda: handle_move_backward(entry_speed, entry_distance, mqtt_sender)

    go_until_button = ttk.Button(frame, text="Go Until")
    go_until_button.grid(row=1, column=4)
    go_until_button['command'] = lambda: handle_go_until(X_entry, delta_entry, entry_speed, mqtt_sender)

    X_entry = ttk.Entry(frame, width=8)
    X_entry.insert(0, "100")
    X_entry.grid(row=3, column=4)
    X_label = ttk.Label(frame, text="Distance from Object")
    X_label.grid(row=2, column=4)

    delta_entry = ttk.Entry(frame, width=8)
    delta_entry.insert(0, "100")
    delta_entry.grid(row=5, column=4)
    delta_label = ttk.Label(frame, text="Delta")
    delta_label.grid(row=4, column=4)




    # Return your frame:
    return frame

def handle_move_forward(entry_speed, entry_distance,mqtt_sender):
    print("move_forward:", entry_distance.get())
    speed=int(entry_speed.get())
    distance=int(entry_distance.get())
    mqtt_sender.send_message("move_forward",[speed, distance])

def handle_move_backward(entry_speed, entry_distance,mqtt_sender):
    print("move_backward:", entry_distance.get())
    speed=(-int(entry_speed.get()))
    distance=int(entry_distance.get())
    mqtt_sender.send_message("move_backward",[speed, distance])


def handle_go_until(entry_speed, X_entry, delta_entry, mqtt_sender):
    speed=int(entry_speed.get())
    X=int(X_entry.get())
    delta=int(delta_entry.get())
    mqtt_sender.send_message("go_until",[speed,X,delta])




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
