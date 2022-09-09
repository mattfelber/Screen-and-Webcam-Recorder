import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

# SCREEN AND WEBCAM RECORDER. AUTOMATICALLY SAVES THE VIDEO FILES WITH DATETIME AS NAME.
# YOU MAY HIDE THE CAM FROM YOUR SCREEN VIEW AND STILL RECORD IT.


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# --print to figure out the dimensions:
# print(height, width)


# --to name the recording files with the datetime:

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d [%H.%M.%S %p]')
file_name = f'{time_stamp}.mp4'

# --to encode the video:

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_vid = cv2.VideoWriter(file_name, fourcc, 14.0, (width, height))

webcam = cv2.VideoCapture(0)

# Capture screen and webcam:

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()

    cv2.imshow('Capturing', img_final)  # This line makes the capture appear on the screen, delete it if you wish.
    cv2.imshow('Horus', frame)  # Makes webcam visible on-screen. Will still be recorded if you delete this line.
    cv2.moveWindow('Horus', 1280, 550)

    # tweak the img_final[x:x, y:y, :] = frame[x:x, y:y, :] as you wish:
    fr_height, fr_width, _ = frame.shape
    # print(fr_height, fr_width)
    img_final[555:1035, 1280: 1920, :] = frame[0: 1080, 0: 1920, :]
    captured_vid.write(img_final)

    # Set a key to stop the recording.
    if cv2.waitKey(10) == ord('e'):
        break
