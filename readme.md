Computer Systems and Networks IOT Assignment - PET MONITOR

This project, which uses a Pi Camera and a PIR motion sensor attached to a Raspberry Pi 3,
is useful for anyone with a pet such as a cat who would like peace of mind while at work. 
Like in the case of my own cat who might wander for a few days.

So to keep some level of monitoring while I'm away, I've set up the Raspberry Pi next to 
the cat flap so that when she comes through the cat flap, the PIR sensor will be triggered 
which in turn triggers the camera to take a photo of her. This is achieved by writing a Python 
script on the Raspberry Pi.

Once the cat has been detected and a photo has been taken, the data is sent to the Web API 
platform "Wia" which shows the data as an "Event". This Event can be viewed as a jpg image in
the Events Tab. As well as receiving a Photo an email notification is also sent to the User's
email address notifying the USER that the Raspberry Pi has detected motion. This is achieved 
using a "Flow" in Wia linking the Trigger which is the Motion Detected Event, with the Action
which is sending the email. 

catflap.jpg
