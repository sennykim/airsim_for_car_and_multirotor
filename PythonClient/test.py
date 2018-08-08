import setup_path 
import airsim

import sys

import numpy as np
import os
import tempfile
import pprint
import threading

import green_multirotor_client


# connect to the AirSim simulator
client = green_multirotor_client.GreenMultirotorClientPV()
client.__init__

client._take_off()


#state = client.getStatus()
#print("state: %s" % state)

vel_x = float(input("Please enter velocity_x: "))
vel_y = float(input("Please enter velocity_y: "))
mode = input("Please enter mode(FO or MD):")
collision = client._take_action(vel_x,vel_y,mode)
print("collision: %s" % collision)



input_cmd = 'no'
while(input_cmd!='q'):
    input_cmd = input("Please enter cmd\n(c: continue \nr: reset \nq: quit \nt: taking image\np: get position\ncc: checking collision\ns: get sensor info): \n")
    if input_cmd=='q':
        client.armDisarm(False)
        client.reset()
        client.enableApiControl(False)
    elif input_cmd == 'r':
        state = client._reset()
        #print("state: %s" % state)
    elif input_cmd == 'c':
        vel_x = float(input("Please enter velocity_x: "))
        vel_y = float(input("Please enter velocity_y: "))
        mode = input("Please enter mode(FO or MD):")
        collision = client._take_action(vel_x,vel_y, mode)
        
        #state = client._get_state()
        print("collision: %s" % collision)
    elif input_cmd == 'cc':
        collision = client._get_collision()
        print("collision: ", collision)
    elif input_cmd == 't':
        state = client._get_state()
    elif input_cmd == 'p':
        state = client._get_position()
        print("position: %s" % pprint.pformat(state))
    elif input_cmd == 's':
        state = client._get_sensor_info()
        print("sensor info: %s" % state)
    else:
        input_cmd = input("Invalid cmd, Please re-enter cmd(c for continue / r for reset / q for quit): ")



