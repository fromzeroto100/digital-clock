import sys, time
import sevseg

try:
    while True: # main program loop.
        # Clear the screen by printing several newlines:
        print('\n' *60)

        # Get the current time from the computers clock:
        currentTime = time.localtime()
        # % 12 so we use a 12-hour clock, not 24:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12' #12-hour clock show 12:00, not 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)    

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopROw, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopROw, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopROw, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(hTopROw    + '      ' + mTopROw     + '     ' + sTopROw)
        print(hMiddleRow + '      ' + mMiddleRow  + '     ' + sMiddleRow)
        print(hBottomRow + '      ' + mBottomRow  + '     ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit')

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    print('Digital clock')
    sys.exit()


