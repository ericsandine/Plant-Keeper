import gpiozero
from time import sleep

pump_1 = gpiozero.OutputDevice(17, active_high=False, initial_value=False)
pump_1.off()

while True:
    pump_1.on()
    print(pump_1)
    print("ON")
    sleep(2)
    pump_1.off()
    print("OFF")
    print(pump_1)
    sleep(2)