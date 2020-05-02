# simple basic example - ESP32 - Micropython - EDU_KIT1
# ROBOTboard with "BUILT_IN_LED", "WS RGB_LED" and "disp7"

from time import sleep
from util.led import Led
from util.rgb import Rgb
from util.octopus import disp7_init
from util.pinout import set_pinout

print("this is simple Micropython example | ESP32 & octopusLAB")

pinout = set_pinout()  # set board pinout
from util.io_config import get_from_file
io_conf = get_from_file()

led = Led(2)
led.blink()

ws = Rgb(pinout.WS_LED_PIN,io_conf.get('ws'))
ws.simpleTest()

d7 = disp7_init()  # 7segment (8digit) display init

sleep(2)
for i in range(9):
    d7.show(10-i)
    sleep(0.3)
d7.show("")
