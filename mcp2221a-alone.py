# set OS environment variable
import os; os.environ["BLINKA_MCP2221"] = "1"

# boards attached
import board
# list supported attached boards
dir(board)

# HID devices
import hid
# lists HID devices, including mice, keyboards and the MCP2221A breakout
# the MCP2221A is seen by the OS as a HID (human interface device)
hid.enumerate()

# import the necessary modules and initialize the I2C bus
device = hid.device()
device.open(0x04D8, 0x00DD)

i2c = board.I2C()
  
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15
  
# create ADC object to talk to the ADS converter
# gives an error if no ADS1115 is found
ads = ADS1115(i2c)    

chan = AnalogIn(ads, ads1x15.Pin.A0)
print(chan.value, chan.voltage)
