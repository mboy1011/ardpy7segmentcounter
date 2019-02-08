from pyfirmata import Arduino, util
from time import sleep
def main():
    try:
        board = Arduino('/dev/ttyACM0') # Port for Arduino Uno 3
        arr = [
            [1,1,1,1,1,1,0],
            [0,1,1,0,0,0,0],
            [1,1,0,1,1,0,1],
            [1,1,1,1,0,0,1],
            [0,1,1,0,0,1,1],
            [1,0,1,1,0,1,1],
            [0,0,1,1,1,1,1],
            [1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1]
        ]
        # Number as Index = Pin Arrangement Ex. arr[0] = [1,1,1,1,1,1,0] equivalent to Pin Arrangement
        pin = [13,7,10,9,8,11,12] # Pin Arrangement [a1,b1,c1,d1,e1,f1,g1]
        def asc():
            #################
            # Ascending 0-9 #
            #################
            for o in range(len(arr)):
                board.digital[6].write(1) # Dp1 Pin
                # sleep(1)
                for i in range(7):
                    # print(f"Pin:{pin[i]} Status:{arr[o][i]}\n")
                    board.digital[pin[i]].write(arr[o][i])
                board.digital[6].write(0)
                sleep(1)
        def desc():
            ##################
            # Descending 9-0 #
            ##################
            for o in range(len(arr)-1,-1,-1): # Count From 9-0 
                board.digital[6].write(1) # Dp1 Pin
                # sleep(1)
                for i in range(6,-1,-1): # Count From 6-0
                    # print(f"{arr[o][i]}")
                    board.digital[pin[i]].write(arr[o][i])
                board.digital[6].write(0)
                sleep(1)
        asc()
    except util.serial.serialutil.SerialException: 
        print("Try run: sudo python3 arduino.py")

if __name__ == "__main__":
    main()