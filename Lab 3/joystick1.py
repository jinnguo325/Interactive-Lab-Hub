import qwiic_joystick
import time
import sys
import ##

def runExample():

	print("\nSparkFun qwiic Joystick   Example 1\n")
	myJoystick = qwiic_joystick.QwiicJoystick()

	if myJoystick.is_connected() == False:
		print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myJoystick.begin()

	print("Initialized. Firmware Version: %s" % myJoystick.get_version())

	while True:
        x = myJoystick.horizontal
        y = myJoystick.vertical
        
        if x > 575:
            #select language A
            
        elif x < 450:
            #select language B
            
        if y > 575:
            #select language c
        elif y <450:
            #select action D


        
