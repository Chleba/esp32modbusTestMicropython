import network
import uwebsockets.client as wsclient
# from umodbus.tcp import ModbusTCPMaster
from time import sleep
from config import wifi, displayTexts

global wlan, connecting, msgNum, modbusCon
connecting = False
msgNum = 0

def activateWifi():
  global wlan
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)

def scanWifi():
  global wlan
  global displayTexts
  scan = wlan.scan()
  for i, s in enumerate(scan):
    if (i < 5):
      displayTexts[i] = "w: {}, s: {}".format(str(s[0], 'utf-8'), str(s[3]))
    print(s)

def modbusConnect():
  global modbusCon
  tcp_device = ModbusTCPMaster(
      slave_ip='192.168.88.248',  # IP address of the target/client/slave device
      slave_port=502,         # TCP port of the target/client/slave device
      # timeout=5.0           # optional, timeout in seconds, default 5.0
  )
  slave_addr = 10
  coil_address = 123
  coil_qty = 1
  coil_status = host.read_coils(
      slave_addr=slave_addr,
      starting_addr=coil_address,
      coil_qty=coil_qty)
  print('Status of coil {}: {}'.format(coil_status, coil_address))

def wshello():
  # global connecting
  # print("wshello connecting")
  # print(str(connecting))
  # if not connecting:
  #   connecting = True
  try:
    with wsclient.connect('ws://192.168.88.148:5000') as websocket:
      global msgNum
      msgNum += 1
      name = 'ESP32T-DISPLAY maslochod id: {}'.format(msgNum)
      websocket.send(name)
      print("> {}".format(name))

      greeting = websocket.recv()
      print("< {}".format(greeting))
  except OSError as osr:
    print(osr)
    # connecting = False
    pass

def wifiThreadFn():
  global wifi, connecting
  # connecting = False
  while True:
    scanWifi()
    print("thread tick connected")
    print(connecting)
    if not wlan.isconnected():
      if not connecting:
        print('Connecting to WiFi ...')
        try:
          wlan.connect(wifi["name"], wifi["pasw"])
          connecting = True
        except OSError as osr:
          print('WiFi connect error')
          print(osr)
          connecting = False
          pass
    else:
      # modbusConnect()
      wshello()
    print("wlan connected: {}".format(str(wlan.isconnected())))  
    sleep(2)