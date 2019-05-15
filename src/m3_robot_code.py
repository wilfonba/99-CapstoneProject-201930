"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Elijah Huff.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_robot_code as m1
import m2_robot_code as m2


class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.
    def arm_up(self, speed):
        self.robot.arm_and_claw.motor.turn_on(speed)
        while True:
            if self.robot.arm_and_claw.touch_sensor.is_pressed():
                        break
        self.robot.arm_and_claw.motor.turn_off()

    def calibrate_arm(self, speed):
        self.arm_up(speed)
        self.robot.arm_and_claw.motor.reset_position()
        self.robot.arm_and_claw.motor.turn_on(-speed)
        while True:
            if abs(self.robot.arm_and_claw.motor.get_position()) >= (360 * 14.2):
                break
        self.robot.arm_and_claw.motor.turn_off()
        self.robot.arm_and_claw.motor.reset_position()

    def arm_to(self, speed, new_position):
        if new_position < self.robot.arm_and_claw.motor.get_position():
            self.robot.arm_and_claw.motor.turn_on(-speed)
            while True:
                if abs(self.robot.arm_and_claw.motor.get_position()) <= new_position:
                    break
        else:
            self.robot.arm_and_claw.motor.turn_on(speed)
            while True:
                if abs(self.robot.arm_and_claw.motor.get_position()) >= new_position:
                    break
        self.robot.arm_and_claw.motor.turn_off()

    def arm_down(self, speed):
        self.arm_to(speed, 0)


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

