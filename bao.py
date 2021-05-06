import time
import wiringpi
import btcom
import btpycom

#setting default values, dont change
wiringpi.wiringPiSetupGpio()
#blake and owen... super important, make sure you plug into port 18....
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 
delay_period = 0.01
end = false

def onStateChanged(state, msg):
    global reply
    if state == "CONNECTING":
        print "Connecting", msg
    elif state == "CONNECTION_FAILED":
        print "Connection failed", msg
    elif state == "CONNECTED":
        print "Connected", msg
    elif state == "DISCONNECTED":
        print "Disconnected", msg
    elif state == "MESSAGE":
        print "Message", msg
        reply = msg
while not end:
    serviceName = "K"
    print(f"searching for: {serviceName}")
    client = BTClient(stateChanged = onStateChanged)
    serverInfo = client.findService(serviceName, 20)
    if serverInfo == None:
        print "Service search failed"
    else:
        print(f"server info: {serverInfo}")
        if client.connect(serverInfo, 20):
            for n in range(50, 250):
                #motor control here ...
                wiringpi.pwmWrite(18, n)
#my github is https://github.com/StonedPaul ... hoes better get an A on this