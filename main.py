from time import sleep
import display
import wifi
import _thread

wifi.activateWifi()
display.startDisplay()

_thread.start_new_thread(wifi.wifiThreadFn, ())

while True:
    display.renderDisplay()
