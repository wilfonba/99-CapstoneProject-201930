"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Ben Wilfong.
  Spring term, 2018-2019.
"""
# Done 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3

#########################################################################


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Ben Wilfong")
    frame_label.grid(row=0, column=0, columnspan=2)
    # Done 2: Put your name in the above.

    # speed_entry = ttk.Entry(frame, width=10)
    # speed_entry.grid(row=1, column=1)

    speed_slider = ttk.Scale(frame, from_=0, to=100)
    speed_slider.set(50)
    speed_slider.grid(row=1, column=1)

    speed_entry_label = ttk.Label(frame, text='Speed (0 - 100)')
    speed_entry_label.grid(row=1, column=0)

    distance_entry = ttk.Entry(frame, width=10)
    distance_entry.insert(0, "50")
    distance_entry.grid(row=2, column=1)

    distance_entry_label = ttk.Label(frame, text='Distance in Degrees')
    distance_entry_label.grid(row=2, column=0)

    spin_left_button = ttk.Button(frame, text='Spin Left')
    spin_left_button.grid(row=3, column=0)

    spin_right_button = ttk.Button(frame, text='Spin Right')
    spin_right_button.grid(row=3, column=1)

    spin_left_button['command'] = lambda: handle_spin_left(
        speed_slider, distance_entry, mqtt_sender)
    spin_right_button['command'] = lambda: handle_spin_right(
        speed_slider, distance_entry, mqtt_sender)

################################################################################

    spin_until_facing_label = ttk.Label(frame, text="Spin Until")
    spin_until_facing_label.grid(column=3, row=0, columnspan = 4)

    speed_label_for_spin_until = ttk.Label(frame, text="Speed 0-100")
    speed_label_for_spin_until.grid(column=3, row=1)
    speed_entry_for_spin_until = ttk.Entry(frame, width=4)
    speed_entry_for_spin_until.grid(column=4, row=1)

    x_label_for_spin_until = ttk.Label(frame, text='X')
    x_label_for_spin_until.grid(column=5, row=1)
    x_entry_for_spin_until = ttk.Entry(frame, width=4)
    x_entry_for_spin_until.grid(column=6, row=1)

    big_enough_label_for_spin_until = ttk.Label(frame, text="Size")
    big_enough_label_for_spin_until.grid(column=3, row=2)
    big_enough_entry_for_finding_spin_until = ttk.Entry(frame, width=4)
    big_enough_entry_for_finding_spin_until.grid(column=4, row=2)

    delta_label_for_spin_until = ttk.Label(frame, text="Delta")
    delta_label_for_spin_until.grid(column=5, row=2)
    delta_entry_for_spin_until = ttk.Entry(frame, width=4)
    delta_entry_for_spin_until.grid(column=6, row=2)

    spin_until_button = ttk.Button(frame, text="Spin Until")
    spin_until_button.grid(column=3, row=3, columnspan=4)

    spin_until_button['command'] = lambda: handle_spin_until(speed_entry_for_spin_until,
                                                              x_entry_for_spin_until,
                                                              big_enough_entry_for_finding_spin_until,
                                                              delta_entry_for_spin_until,
                                                              mqtt_sender)

#######################################################################################################

    dance_button = ttk.Button(frame, text="Dance!")
    dance_button.grid(row=8, column=0)

    dance_colors_entry = ttk.Entry(frame)
    dance_colors_entry.grid(row=8, column=1, columnspan=7)
    dance_colors_entry.insert(0, "Black, White, Red, Yellow, Blue")

    dance_button['command'] = lambda: handle_dance(dance_colors_entry, mqtt_sender)

    # Return your frame:
    return frame

###########################################################################


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

##########################################################################


def handle_spin_left(speed_entry, distance_entry, sender):
    print("handle_spin_left: ", speed_entry.get(), distance_entry.get())
    speed = int(speed_entry.get())
    distance = int(distance_entry.get())
    sender.send_message("spin_left", [speed, distance])


def handle_spin_right(speed_entry, distance_entry, sender):
    print("handle_spin_right: ", speed_entry.get(), distance_entry.get())
    speed = int(speed_entry.get())
    distance = int(distance_entry.get())
    sender.send_message("spin_right", [speed, distance])


def handle_spin_until(speed_entry, x_entry, big_enough_entry, delta_entry, sender):
    print("handle_spin_until", speed_entry.get, x_entry.get, big_enough_entry.get(),
          delta_entry.get())
    speed = int(speed_entry.get())
    x = int(x_entry.get())
    big_enough = int(big_enough_entry.get())
    delta = int(delta_entry.get())
    sender.send_message("spin_until", [speed, x, big_enough, delta])


def handle_dance(color_entry, sender):
    color_entry_string = color_entry.get()
    colors = []
    individual_color = ""
    for k in range(len(color_entry_string)):
        if color_entry_string[k] == ",":
            colors.append(individual_color)
            individual_color = ""
        else:
            individual_color += color_entry_string[k]
    print("handle_dance", colors)
    sender.send_message("dance", [colors])
