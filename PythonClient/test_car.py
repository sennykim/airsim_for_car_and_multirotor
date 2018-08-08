from AirSimClient import *

# connect to the AirSim simulator 


import car_client_for_rl


# connect to the AirSim simulator
client = car_client_for_rl.CarClientForRL()
client.__init__



#state = client.getStatus()
#print("state: %s" % state)

throttle = float(input("Please enter throttle: "))
steering = float(input("Please enter steering: "))

client._take_car_action(throttle,steering)

input_cmd = 'no'
while(input_cmd!='q'):
    input_cmd = input("Please enter cmd\n(c: continue \nr: reset \nq: quit): \n")
    if input_cmd=='q':
        client.reset()
        client.enableApiControl(False)
    elif input_cmd == 'r':
        client._reset_car()
        #print("state: %s" % state)
    elif input_cmd == 'c':
        throttle = float(input("Please enter throttle: "))
        steering = float(input("Please enter steering: "))
        client._take_car_action(throttle,steering)
    else:
        input_cmd = input("Invalid cmd, Please re-enter cmd(c for continue / r for reset / q for quit): ")
