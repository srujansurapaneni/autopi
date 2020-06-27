from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep
import cv2
import numpy as np
import picar
import os
picar.setup()

########       Driving code       #######################

bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()

bw.speed = 30
bw.stop()

########       camera capture and save       ############

# single image capture
img = cv2.VideoCapture(-1)
SCREEN_WIDTH = 160
SCREEN_HIGHT = 120
img.set(3,SCREEN_WIDTH)
img.set(4,SCREEN_HIGHT)
CENTER_X = SCREEN_WIDTH/2
CENTER_Y = SCREEN_HIGHT/2
bgr_image = img.read()[1]

# save image to a specific path
cv2.imwrite('/home/pi/Pictures/Image.jpg',bgr_image)

