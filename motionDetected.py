from wia import Wia
import time
from gpiozero import MotionSensor
from picamera import PiCamera


wia = Wia()
## INSERT YOUR SECRET KET
wia.access_token = 'd_sk_LdxRJf6kfHPPITGFj37EUUuU'
camera = PiCamera()
pir = MotionSensor(7)


def motionDetected():
    print("Motion Detected")
    takePhoto()

## defining takePhoto method
def takePhoto():
    camera.capture('/home/pi/image.jpg')
    time.sleep(5)
    sendToWiaPlatform()

## method to  publish to 'motionDetected' Widget
def sendToWiaPlatform():
    wia.Event.publish(name='motionDetected', file=open('/home/pi/image.jpg', 'rb'))

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    takePhoto() 
    time.sleep(15)
    pir.wait_for_no_motion()
    print("No Motion")
