import network
import uwebsockets.client as wsclient
from time import sleep
from config import wifi, displayTexts

global wlan, connecting, msgNum
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
      wshello()
    print("wlan connected: {}".format(str(wlan.isconnected())))  
    sleep(2)