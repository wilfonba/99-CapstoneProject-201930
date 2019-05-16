"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Ben Wilfong.
  Spring term, 2018-2019.
"""
# Done 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3

##########################################################################


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

    def stop(self):
        """ Tells the robot to stop moving. """
        print_message_received("stop")
        self.robot.drive_system.stop()

    def spin_left(self, speed, distance):
        """Makes the robot spin left x degrees"""

        print_message_received("spin_left", [speed, distance])
        self.robot.drive_system.left_motor.turn_on(-speed)
        self.robot.drive_system.right_motor.turn_on(speed)
        while True:
            if self.robot.drive_system.right_motor.get_position() >= distance*5.5:
                self.robot.drive_system.right_motor.reset_position()
                self.robot.drive_system.left_motor.reset_position()
                self.robot.drive_system.stop()
                break
        return

    def spin_right(self, speed, distance):
        """Makes the robot spin right x degrees"""

        print_message_received("spin_right", [speed, distance])
        self.robot.drive_system.left_motor.turn_on(speed)
        self.robot.drive_system.right_motor.turn_on(-speed)
        while True:
            if self.robot.drive_system.left_motor.get_position() >= distance*5.5:
                self.robot.drive_system.stop()
                self.robot.drive_system.right_motor.reset_position()
                self.robot.drive_system.left_motor.reset_position()
                break
        return

    def spin_until(self, speed, x, big_enough, delta):
        """Turns until signature 1 with set speed to an object who's area is big_enough
        and spins until the object has the x coordinate x plus or minus delta"""

        print_message_received("spin_until", [speed, x, big_enough, delta])
        self.robot.drive_system.left_motor.turn_on(speed)
        self.robot.drive_system.right_motor.turn_on(-speed)
        while True:
            biggest_blob = self.robot.sensor_system.camera.get_biggest_blob()
            if abs(x - biggest_blob.center.x) <= delta and biggest_blob.get_area() >= big_enough:
                self.robot.drive_system.left_motor.turn_off()
                self.robot.drive_system.right_motor.turn_off()
                break

        return

#########################################################################


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)
