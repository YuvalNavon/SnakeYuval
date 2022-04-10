WOW_NUMBER = 1
MAX_WOW_SHOTS = 3
MIN_WOW_DISTANCE = 10
MAX_NICE_SHOTS = 6
MIN_NICE_DISTANCE = 8
MAX_OK_SHOTS = 10
MIN_OK_DISTANCE = 4
MIN_VALID_VALUE = 0


def main():
    distance = int(input("Insert distance"))
    shots = int(input("Insert number of shots"))
    if (shots<MIN_VALID_VALUE or distance<MIN_VALID_VALUE): print ("Invalid value")
    elif ((distance == WOW_NUMBER and shots == WOW_NUMBER) or (shots<MAX_WOW_SHOTS and distance>MIN_WOW_DISTANCE)): print ("WOW")
    elif (shots<MAX_NICE_SHOTS and distance>MIN_NICE_DISTANCE): print ("NICE")
    elif (shots<MAX_OK_SHOTS and distance>MIN_OK_DISTANCE): print ("OK")
    else:
        ans = input("do you feel ok?")
        if (ans=="no"): print ("Take five")
        else: print ("Try again")





if __name__ == '__main__':
    main()