# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import pigpio
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# led
GPIO_R = 13 
GPIO_G = 26
GPIO_B = 19

# led initalaze
normalize = 255.0 / 1024 # pwm maximum / 10 bits
pi = pigpio.pi()
pi.set_PWM_frequency(GPIO_R,200)
pi.set_PWM_frequency(GPIO_G,200)
pi.set_PWM_frequency(GPIO_B,200)

# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i) * normalize
    
    #led data send
    pi.set_PWM_dutycycle(GPIO_R,values[0])
    pi.set_PWM_dutycycle(GPIO_G,values[1])
    pi.set_PWM_dutycycle(GPIO_B,values[2])

    # Print the ADC values.
    print('R| {0:>3.1f}   G|{1:>3.1f}   B|{2:>3.1f}'.format(*values))
    time.sleep(0.5)
