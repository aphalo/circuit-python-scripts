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

import adafruit_dacx578 

# Initialize I2C and DAC
dac1 = adafruit_dacx578.DACx578(i2c, 0x4C)
dac2 = adafruit_dacx578.DACx578(i2c, 0x48)

import math
import time

MAX_VALUE = 65535  # 16-bit value but resolution is 10 bit = 1024, 
ch_dimm = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
global_dim = 1

for channel_num in range(8):
    dac1.channels[channel_num].value = round((1 - global_dim * ch_dimm[channel_num]) * MAX_VALUE)
    dac2.channels[channel_num].value = round((1 - global_dim * ch_dimm[channel_num + 8]) * MAX_VALUE)

# The current value of the DAC register can be read
for channel_num in range(8):
    print(dac1.channels[channel_num].value)
    print(dac2.channels[channel_num].value)

# There is a single clock and divider, so all channels use the
# same frequency, while duty cycle can be set per channel
import adafruit_pca9685
pca = adafruit_pca9685.PCA9685(i2c_bus = i2c, reference_clock_speed=25509888)

# PWM frequency in Hz (range 40 to 1500) shared by all channels
pca.frequency = 200
# Settings are done by first selecting a channel
# PWM board channels 0 to 15
led_channel = pca.channels[0]
# Duty cycle 0x0000 to 0xffff
led_channel.duty_cycle = 0xffff
led_channel.duty_cycle = 0xf330
led_channel.duty_cycle = 0x7fff
led_channel.duty_cycle = 0x1fff
led_channel.duty_cycle = 0x05ff
led_channel.duty_cycle = 0x0000

from adafruit_mcp230xx.mcp23017 import MCP23017
mcp_dio = MCP23017(i2c)

# Set as output and control pins individually
# --- using high-level functions to access them
# pin0 = mcp_dio.get_pin(0)
# pin0.switch_to_output(value=True)
# pin0.switch_to_output(value=False)

# pin15 = mcp_dio.get_pin(15)
# pin15.switch_to_output(value=True)
# pin15.switch_to_output(value=False)

# set all pins as output and control them in block by Port by setting
# registers in the MCP23017 
#  --- using loop to set the registers one bit/pin at a time
# for pin in range(16):  # Configure pins 0-7 (Port A) and 0-7 (Port B) as outputs
#    mcp_dio.get_pin(pin).switch_to_output()
#  --- writing to registers for Ports A and B
#  mcp_dio.iodira = 0x00
#  mcp_dio.iodirb = 0x00
#  --- writing all bits to the register at once
mcp_dio.iodir = 0x00

# Set state of pins, one port at time
mcp_dio.gpioa = 0xFF 
mcp_dio.gpioa = 0x00 

mcp_dio.gpiob = 0xFF 
mcp_dio.gpiob = 0x00 

# Control both ports simultaneously
mcp_dio.gpio = 0xFF 
mcp_dio.gpio = 0x00

import adafruit_ds3231
import time
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

ds3231 = adafruit_ds3231.DS3231(i2c)
ds3231.datetime    
ds3231.datetime = time.struct_time((2026, 9, 22, 18, 26, 0, 1, -1, -1))

t = ds3231.datetime
print(f"The date is {days[int(t.tm_wday)]} {t.tm_mday}/{t.tm_mon}/{t.tm_year}")
print(f"The time is {t.tm_hour}:{t.tm_min:02}:{t.tm_sec:02}")

ds3231.temperature

ds3231.alarm1_status
ds3231.alarm1_interrupt
ds3231.alarm1

ds3231.alarm2_status
ds3231.alarm2_interrupt
ds3231.alarm2
