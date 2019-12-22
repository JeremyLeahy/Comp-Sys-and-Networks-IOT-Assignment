from wia import Wia
import time
from gpiozero import MotionSensor
from picamera import PiCamera


wia = Wia()
## INSERT YOUR SECRET KET
wia.access_token = 'd_sk_LdxRJf6kfHPPITGFj37EUUuU'
camera = PiCamera()
pir = MotionSensor(7)


## defining takePhoto method
def takePhoto():
    camera.start_preview()
    time.sleep(1)
    camera.capture('/home/pi/image.jpg')
    time.sleep(5)
    sendToWiaPlatform()

## method to  publish to 'motionDetected' Widget
def sendToWiaPlatform():
    wia.Event.publish(name='motionDetected', file=open('/home/pi/image.jpg', 'rb'))

##Delay initially set to allow motion sensor to initialize and learn environment
time.sleep(30)

while True:
    time.sleep(3)
    pir.wait_for_motion()
    print("Motion Detected")
    takePhoto() 
    time.sleep(15)
    pir.wait_for_no_motion()
    print("No Motion")
