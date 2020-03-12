def burglar() :
	print("test Burglar") 
	red, green, blue, clear =light_sensor.safe_raw_colors()
	if clear > 0.015: #Tant que la lumière est faible
		sound_percentage = sound_sensor.percent_read()
		if sound_percentage > 5 : #valeur à vérifier
			if motion_sensor.motion_detected() : 
				tweet("Attention! Je crois que un intru tente de pénétrer votre domicile !")
			un = sound_percentage
			tab = [un]
			gopigo.turn_degrees(90)
			sleep(1)
			deux = sound_sensor.percent_read()
			tab.append(deux)
			gopigo.turn_degrees(90)
			sleep(1)
			trois = sound_sensor.percent_read()
			tab.append(trois)
			gopigo.turn_degrees(90)
			sleep(1)
			quatre = sound_sensor.percent_read()
			tab.append(quatre)
			#print("Le max est", max(tab))
			for i in range(len(tab)):
				if tab[i] == max(tab):
					gopigo.turn_degrees(90*i)
			gopigo.open_eyes()
			gopigo.forward()
			sleep(10)
			gopigo.stop()		
		sleep(0.5)
	sleep(0.5)

def light_on() :
	print("test light_on") 
	red, green, blue, clear =light_sensor.safe_raw_colors()
	timer = 0
	#print(clear)
	red, green, blue, clear = light_sensor.safe_raw_colors()
	if clear<0.011 :
		if (sound_sensor.percent_read() > 3.90) or motion_sensor.motion_detected():
		    timer=0
		else : #plus la lumière est forte plus elle s'approche de 0
			if timer>180 : #3 minutes
				tweet ("Attention lumière restée allumée")
				sys.exit()
		sleep(0.5)
		timer +=0.5
	else :
	    timer =0

def tv_on() :
    print("test tv_on")
    compteur = 0
    sound_percentage= 0
    sound_value = sound_sensor.percent_read()
    sound_percentage = (sound_value+n*sound_percentage)/(n+1) 
        if motion_sensor.motion_detected() : #human detected
            compteur=0
        elif compteur>10 : #180
            tweet("Je pense que la télévision est restée allumée")
            sys.exit()
    else :
        compteur =0
    sleep(0.5)
    compteur +=0.5

def chauffage_allume() :
	print("test chauffage_allumé")
	n = 0
	temp = imu.read_temperature()
	sound_percentage = sound_sensor.percent_read()
	if ((sound_percentage > 3.93) or motion_sensor.motion_detected()) : #human detected
	    n=0
	elif temp> 20 : #température conseillée avec chauffage entre 18°C et 20°C
	    if n>900 : # 15 min
	        tweet("Je crois tu as laissé un chauffage allumée")
	        sys.exit()
	sleep(0.5)
	n +=0.5


def fenetre_ouverte() :
	print("test fenêtre_ouverte")
	cpt = 0
	temp = imu.read_temperature()
	    if (temp > 16 ) : #température conseillée pour les chambres la nuit : 16°C mais pas plus bas
	            cpt=0
	    elif cpt>3600 :
	            tweet("Attention fenêtre ouverte")
	            sys.exit()
	    sleep(0.5)
	    cpt +=0.5



import easygopigo3 as easy
from time import sleep
from send.py import tweet
from di_sensors.easy_light_color_sensor import EasyLightColorSensor 
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit
import sys
gopigo = easy.EasyGoPiGo3() #declaration du robot
light_sensor = EasyLightColorSensor(led_state = False)  #declaration du light_sensor
	
port2 = "AD2" #declaration soud_sensor
sound_sensor = gopigo.init_sound_sensor(port2)
	
port1 = "AD1" #declaration motion_sensor
motion_sensor = gopigo.init_motion_sensor(port1)

imu = InertialMeasurementUnit() #declaration inertial mesurment unit sensor

if __name__ == "__main__":
    while True :
 		sound_percentage = sound_sensor.percent_read()
 		motion_sensor.motion_detected()
 		red, green, blue, clear = light_sensor.safe_raw_colors()
 		temp = imu.read_temperature()

		burglar() 
		light_on()
		tv_on()
		chauffage_allumee()
		fenetre_ouverte()

