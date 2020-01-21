import time
from picamera import PiCamera

# source: https://picamera.readthedocs.io/en/release-1.13/index.html
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

# Camera warm-up time
time.sleep(5)
camera.capture('./files/foo.jpg')
