from machine import Pin

import ds18x20
import onewire
import time

dsPin = Pin(22)
print('dsPin: ', dsPin)
dsSensor = ds18x20.DS18X20(onewire.OneWire(dsPin))
print('dsSensor: ', dsSensor)
roms = dsSensor.scan()
print('Found DS devices: ', roms)

while True:
    dsSensor.convert_temp()
    time.sleep_ms(750)
 
    for rom in roms:
        print(rom)
        print(dsSensor.read_temp(rom))
        time.sleep(5)
        