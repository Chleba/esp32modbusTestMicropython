from machine import Pin, SoftSPI
import st7789py as st7789
from romfonts import vga2_8x16 as font
from config import displayTexts, prevDisplayTexts 

def startDisplay():
  spi = SoftSPI(
      baudrate=20000000,
      polarity=1,
      phase=0,
      sck=Pin(18),
      mosi=Pin(19),
      miso=Pin(13))

  global tft
  tft = st7789.ST7789(
      spi,
      135,
      240,
      reset=Pin(23, Pin.OUT),
      cs=Pin(5, Pin.OUT),
      dc=Pin(16, Pin.OUT),
      backlight=Pin(4, Pin.OUT),
      rotation=0)
  tft.rotation(3)
  tft.fill(0)

def renderDisplay():
  global displayTexts, prevDisplayTexts
  for i, t in enumerate(displayTexts):
    if t != prevDisplayTexts[i]:
      tft.fill_rect(0, int(i * 16), tft.width, 16, st7789.color565(0, 0, 0))
      tft.text(
        font,
        str(t, 'utf-8'),
        0,
        int(i * 16),
        st7789.color565(200, 200, 200),
        st7789.color565(0, 0, 0)
      )
      prevDisplayTexts[i] = t
