import smbus
import time

bus = smbus.SMBus(1)

DEVICE = 0x23

def readLight(address = DEVICE):
    data = bus.read_i2c_block_data(address, DEVICE)
    result = (data[1] + (256 * data[0])) / 1.2
    return result

try:
    while 1:
        lightLevel = readLight()
        print("Light level")
        
        if (lightLevel <= 20):
            print("Too dark")
        elif(lightLevel > 50) and (lightLevel <= 200):
            print("Dark")
        elif(lightLevel > 200) and (lightLevel <= 500):
            print("Medium")
        elif(lightLevel > 500) and (lightLevel <= 1000):
            print("Bright")
        else:
            print("Too Bright")
        time.sleep(0.25)
        
except KeyboardInterrupt:
    print("Stop")
    