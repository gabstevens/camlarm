from gpiozero import MotionSensor
import time

def allarme_movimento1():
    print("Movimento rilevato 1")


def allarme_movimento2():
    print("Movimento rilevato 2")

pir_1 = MotionSensor(pin=4, pull_up=False)
pir_2 = MotionSensor(pin=17, pull_up=False)

pir_1.when_motion = allarme_movimento1
pir_2.when_motion = allarme_movimento2

print("Inizializzazione PIR: in attesa di movimento...")

while True:
    time.sleep(0.5)

"""     print(str(pir_1.is_active) +" sensore 1")
    print(str(pir_2.is_active) + " sensore 2") """
 

