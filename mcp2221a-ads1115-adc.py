# Using Blinka library to emulate CircuitPhyton in computer
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

# I2C (MCP2221A is the controller or "master")
i2c = board.I2C()
  
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15

# create ADC object to talk to the ADS converter
# gives an error if no ADS1115 is found
# I2C (ADS1115 is a peripheral or "slave")
ads = ADS1115(i2c)    

# 4 channels are available A0, A1, A2 and A3
chA0 = AnalogIn(ads, ads1x15.Pin.A0)
chA1 = AnalogIn(ads, ads1x15.Pin.A1)
chA2 = AnalogIn(ads, ads1x15.Pin.A2)
chA3 = AnalogIn(ads, ads1x15.Pin.A3)

# value are the raw counts
# voltage is the voltage based on ADC calibration
print(chA0.value, chA0.voltage)
print(chA0.voltage, chA1.voltage, chA2.voltage, chA3.voltage)
print(round(chA0.voltage, 3), chA1.voltage, chA2.voltage, chA3.voltage)
# PGA (programmable gain amplifier)
# Gain is always the same for all 4 channels!
print(ads.gains) # allowed values
ads.gain = 1
print(chA0.value, chA0.voltage)
ads.gain = 16
print(chA0.value, chA0.voltage)
ads.gain = 1
