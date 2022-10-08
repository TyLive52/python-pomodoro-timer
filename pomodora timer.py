#set up the timer and create a function
#we will be going for 45 minutes on, 15 minutes off
#so 45 min timers with 15 minute intervals

while True:


    import time

    t = int(input("How long would you like to study for this session?"))


    print("Hyperbolic Training Begins Now!")
    for i in range(4):
        t = t*60
        while t:
            mins = t// 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("  " + timer, end="\r") #override previous line
            time.sleep(1)
            t -= 1
        print("Take a Break you've earned it!")
        break