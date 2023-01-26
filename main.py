from time import sleep
import display
import wifi
import free
from umodbus.tcp import ModbusTCPMaster
import _thread

wifi.activateWifi()
display.startDisplay()

_thread.stack_size(8192)
_thread.start_new_thread(wifi.wifiThreadFn, ())

while True:
    display.renderDisplay()
