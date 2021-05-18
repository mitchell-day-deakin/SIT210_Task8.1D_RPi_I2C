import time
from smbus import SMBus

i2cbus = SMBus(1)
i2cadd = 0x27


def backLight(inst):
    if inst=="on":
        i2cbus.write_byte(i2cadd, 0x08)
    else:
        i2cbus.write_byte(i2cadd, 0xF0)


def display():
    data = 45
    i2cbus.write_byte_data(i2cadd, 0x02,0xB3)

display()
backLight("on")
time.sleep(1)
backLight("off")
time.sleep(1)
backLight("on")
