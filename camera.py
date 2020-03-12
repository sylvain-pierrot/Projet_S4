#Utiliser la caméra et enregistrer la photo où l'on souhaite
from datetime import datetime
from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview(alpha=192)
now = datetime.now()
name_time=now.strftime("/home/pi/Dexter/GoPiGo3/Software/Python/Examples/nosProg/%d_%H_%M_%S.jpg")
camera.capture(name_time)
camera.stop_preview()