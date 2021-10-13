import qwiic_joystick
import time
import sys
<<<<<<< HEAD
import ##
=======
>>>>>>> b4d5bd532a6b6addaa039b5f2908a4abdbe1af37

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
<<<<<<< HEAD
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

=======
		print("X: %d, Y: %d, Button: %d" % ( \
					myJoystick.horizontal(), \
					myJoystick.vertical(), \
					myJoystick.button()))

		time.sleep(.5)
		
if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)
>>>>>>> b4d5bd532a6b6addaa039b5f2908a4abdbe1af37

        
