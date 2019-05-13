import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)

camera.start_recording('./files/myvideo.h264')
camera.wait_recording(60)
camera.stop_recording()
