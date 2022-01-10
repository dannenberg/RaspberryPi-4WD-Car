import asyncio
import sys
from typing import List
import time

from grpclib.client import Channel

import gen
from proto.api.v1.robot_pb2 import BaseMoveStraightRequest, BaseSpinRequest, BoardGPIOGetRequest, StatusResponse
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
MoveSpeed = 200.0
TurnDistance = 30.0
TurnSpeed = 180.0
grpc_addr = "localhost"
grpc_port = 8080

#Motor pins are initialized into output mode
#Key pin is initialized into input mode
#infrared obstacle avoidance module pins are initialized into input mode
# init removed as all of that work is handled by the viam server.

#advance
async def run(client):
    req = BaseMoveStraightRequest()
    req.name = BaseName
    req.distance_millis = MoveDistance
    req.millis_per_sec = MoveSpeed
    status = await client.BaseMoveStraight(req)

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
async def spin_left(client):
    req = BaseSpinRequest()
    req.name = BaseName
    req.angle_deg = TurnDistance
    req.degs_per_sec = -TurnSpeed
    status = await client.BaseSpin(req)

#turn right in place
async def spin_right(client):
    req = BaseSpinRequest()
    req.name = BaseName
    req.angle_deg = TurnDistance
    req.degs_per_sec = TurnSpeed
    status = await client.BaseSpin(req)

#brake
def brake():
    # implement as needed
    pass

async def read_sensor(client, pin):
    req = BoardGPIOGetRequest()
    req.name = "local"
    req.pin = pin
    status = await client.BoardGPIOGet(req)
    return status.high

# TODO(dannenberg): add button scan in a viam-ish way
def key_scan():
     pass

time.sleep(2)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
async def main(args):
    try:
        #key_scan()
        async with Channel(grpc_addr, grpc_port) as channel:
            client = RobotServiceStub(channel)
            while True:
              #There is obstacle, the indicator light of the infrared obstacle avoidance module is on, and the port level is LOW
              #There is no obstacle, the indicator light of the infrared obstacle avoidance module is off, and the port level is HIGH
                LeftSensorValue  = await read_sensor(client, AvoidSensorLeft)
                RightSensorValue = await read_sensor(client, AvoidSensorRight)
                print ("left:", LeftSensorValue, "right:", RightSensorValue)
                if LeftSensorValue == False and RightSensorValue == False :
                    await run(client)
                elif LeftSensorValue == False and RightSensorValue == True :
                    await spin_left(client)
                    time.sleep(0.002)
                elif RightSensorValue == False and LeftSensorValue == True:
                    await spin_right(client)
                    time.sleep(0.002)
                elif RightSensorValue == True and LeftSensorValue == True :
                    time.sleep(0.002)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    sys.exit(asyncio.run(main(sys.argv)))
