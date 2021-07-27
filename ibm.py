'''https://github.com/gnaneshwarbandari/IOT/blob/main/ibm_code.py
'''

import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "rkpofh",
        "typeId": "VITDevices",
        "deviceId":"2002"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    #m=cmd.data['command']
    #if m == "lighton":
    #    print("Light is on")
    #elif m == "lightoff" :
    #    print("Light is off")
    print()

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    myData={'temperature':temp, 'humidity':hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
