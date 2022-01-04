-*- coding:UTF-8 -*-
import asyncio
import sys
from typing import List
import time

from grpclib.client import Channel

import gen
from proto.api.v1.robot_pb2 import BoardGPIOGetRequest, StatusResponse
from proto.api.v1.robot_grpc import RobotServiceStub

#Definition of  motor pin 
# deleted since base functions cover all our  motor needs

#Definition of  button
# removing the button scan for now

#Definition of infrared obstacle avoidance module pin
# changed from GPIO pin number to pi pin number
# added other constants
AvoidSensorLeft = "32"
AvoidSensorRight = "11"
BoardName = "local"
BaseName = "yahboom-base"
MoveDistance = 10
MoveSpeed = 100.0
TurnDistance = 30.0
TurnSpeed = 90.0

#Motor pins are initialized into output mode
#Key pin is initialized into input mode
#infrared obstacle avoidance module pins are initialized into input mode
# init removed as all of that work is handled by the viam server.

#advance
def run():
    try:
        async with Channel(grpc_addr, grpc_port) as channel:
            client = RobotServiceStub(channel)
            req = BaseMoveStraightRequest()
            req.name = BaseName
            req.distance_millis = MoveDistance
            req.millis_per_sec = MoveSpeed
            status = await client.BaseMoveStraight(req)
    except Exception as e:
        print(e, file=sys.stderr)

#back
def back():
    # implement as needed
    pass

#turn left
def left():
    # implement as needed
    pass

#turn right
def right():
    # implement as needed
    pass

#turn left in place
def spin_left():
    try:
        async with Channel(grpc_addr, grpc_port) as channel:
            client = RobotServiceStub(channel)
            req = BaseSpinRequest()
            req.name = BaseName
            req.angle_deg = -TurnDistance
            req.degs_per_sec = TurnSpeed
            status = await client.BaseSpin(req)
    except Exception as e:
        print(e, file=sys.stderr)

#turn right in place
def spin_right():
    try:
        async with Channel(grpc_addr, grpc_port) as channel:
            client = RobotServiceStub(channel)
            req = BaseSpinRequest()
            req.name = BaseName
            req.angle_deg = -TurnDistance
            req.degs_per_sec = TurnSpeed
            status = await client.BaseSpin(req)
    except Exception as e:
        print(e, file=sys.stderr)

#brake
def brake():
    # implement as needed
    pass

def read_sensor(pin):
    try:
        async with Channel(grpc_addr, grpc_port) as channel:
            client = RobotServiceStub(channel)
            req = BoardGPIOGetRequest()
            req.name = "local"
            req.pin = pin
            status = await client.BoardGPIOGet(req)
            return req.high
    except Exception as e:
        print(e, file=sys.stderr)
        return False #TODO(dannenberg) make this a more sensible failure handling

# TODO(dannenberg): add button scan in a viam-ish way
def key_scan():
     pass
            
time.sleep(2)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
try:
    #key_scan()
    while True:
      #There is obstacle, the indicator light of the infrared obstacle avoidance module is on, and the port level is LOW
      #There is no obstacle, the indicator light of the infrared obstacle avoidance module is off, and the port level is HIGH
        LeftSensorValue  = read_sensor(AvoidSensorLeft);
        RightSensorValue = read_sensor(AvoidSensorRight);

        if LeftSensorValue == True and RightSensorValue == True :
            run()     
        elif LeftSensorValue == True and RightSensorValue == False :
            spin_left()   
            time.sleep(0.002)
        elif RightSensorValue == True and LeftSensorValue == False:
            spin_right()  
            time.sleep(0.002)
        elif RightSensorValue == False and LeftSensorValue == False :
            spin_right()  
            time.sleep(0.002)
       
except KeyboardInterrupt:
    pass
