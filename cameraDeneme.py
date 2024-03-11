from time import sleep
from picamera2 import Picamera2, Preview, libcamera

picma2 = Picamera2()


picma2.start_preview(Preview.QTGL)
sleep(3)
picma2.start()
sleep(30)
'''
picma2.start_and_capture_file("test2.jpg", delay=5)

picma2.start_and_record_video("testvideo.mp4", duration=10, show_preview=True)

'''