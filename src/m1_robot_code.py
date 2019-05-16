"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Maddie Sorensen.
  Spring term, 2018-2019.
"""
# Done:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3


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
        self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def go(self, left_motor_speed, right_motor_speed):
        """ Tells the robot to go (i.e. move) using the given motor speeds. """
        print_message_received("go", [left_motor_speed, right_motor_speed])
        self.robot.drive_system.go(left_motor_speed, right_motor_speed)

    # Done: Add methods here as needed.
    def move_forward(self, speed, distance):
        print('speed', speed, distance)
        self.robot.drive_system.go(speed, speed)
        self.robot.drive_system.left_motor.reset_position()
        while True:
            if (self.robot.drive_system.left_motor.get_position()/85)>=distance:
                self.robot.drive_system.stop()
                break

    def move_backward(self, speed, distance):
        print('speed backward', speed, distance)
        self.robot.drive_system.go(speed,speed)
        self.robot.drive_system.left_motor.reset_position()
        while True:
            if abs((self.robot.drive_system.left_motor.get_position()/85))>=distance:
                self.robot.drive_system.stop()
                break

    def go_until(self,speed,X,delta):
        self.robot.drive_system.left_motor.reset_position()
        original=self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()-X
        go_straight=original*(1/2)
        self.robot.drive_system.go(speed, speed)
        print("go:1")
        while True:
            print("true")
            if abs((self.robot.drive_system.left_motor.get_position()/85))>=go_straight:
                break

        new_speed = (1 / 2) * speed
        self.robot.drive_system.go(new_speed, new_speed)
        print("go:2")
        while True:
            a = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            b = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            c = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            d = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            e = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if a<10000:
                small=a
            if a>0:
                big=a
            if b<small:
                small=b
            if b>big:
                big=b
            if c<small:
                small=c
            if c>big:
                big=c
            if d<small:
                small=d
            if d>big:
                big=d
            if e<small:
                small=e
            if e>big:
                big=e
            average=(a+b+c+d+e-small-big)/3
            if average<=(X+delta) and average>=(X-delta):

                break
        self.robot.drive_system.stop()



def print_message_received(method_name, arguments):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

