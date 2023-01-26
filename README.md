# esp32modbusTestMicropython
Micropython for ESP32 TTGO T-Display with micropython FW. 
Testing examples with implementation of
- ModBus library
- ST7789 display library with romfonts
- WiFi &amp; WebSocket connection
- threads

## Used libraries
- WebSockets: https://github.com/danni/uwebsockets
- ST7789: https://github.com/russhughes/st7789py_mpy
- Modbus: https://github.com/brainelectronics/micropython-modbus

## Micropython FW
- v1.19.1 - https://micropython.org/download/esp32/

## Used tools
- rshell: https://github.com/dhylands/rshell
- esp-idf: https://github.com/espressif/esp-idf
- esptool: https://github.com/espressif/esptool

#
## First run / installations
- connect ESP32 TTGO T-Display with USB to a PC
- download Micropython FW (v1.19.1>)
- erase flash on ESP32
    - `esptool.py --chip esp32 --port /dev/ttyACM0 erase_flash`
- upload new FW onto ESP32
    - `esptool.py --chip esp32 --port /dev/ttyACM0 --baud 460800 -z 0x1000 write_flash ./micropythonfw.bin`
- hard reset ESP32 board
- via rshell connect to the ESP32 
    - `rshell -p /dev/ttyACM0 -b 115200`
- board will mount after connecion it's flash disk into a `/pyboard/` directory
- upload files into that directory via `cp ./files/* /pyboard/`
- after all files is uploaded you may hard reset the ESP32 board
- type `repl` in rshell to see serial outpur

## Usage
<img src="https://github.com/Chleba/esp32modbusTestMicropython/blob/main/example.jpg" width="240" />

This testing App is just trying to make some performance observations.
It will make two threads.
One with rendering scanned WiFi networks on st7789 display.
Second that will work with networking.
Board is doing:
- create two threads
- create station WiFi
- every 2.seconds scan WiFi networks
- every 2.seconds create WebSocket client & connect to WebSocket server to send & recieve message
- outputing debug messages into a USB serial
- rendering scaned WiFi's to display
- creating text file with R/W on flash storage
- !!! implemented umodbus library BUT *getting allocation memory fail error* - TODO (need more work with used memory on ESP32 board)