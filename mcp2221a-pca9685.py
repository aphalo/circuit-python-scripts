# set OS environment variable
import os
os.environ["BLINKA_MCP2221"] = "1"

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

import adafruit_pca9685
pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 500
led_channel = pca.channels[0]
led_channel.duty_cycle = 0xffff
led_channel.duty_cycle = 0xf330
led_channel.duty_cycle = 0x7fff
led_channel.duty_cycle = 0x1fff
led_channel.duty_cycle = 0x05ff
led_channel.duty_cycle = 0x0000
