#   To check address: sudo i2cdetect -y 1

import smbus
import time

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

class Joystick:
  def __init__(self,address,xchn,ychn):
    self.PCF8591 = PCF8591(address)
    self.xchn = xchn
    self.ychn = ychn
  def getX(self,xchn):
    return self.PCF8591.read(self,xchn)
  def getY(self,ychn):
    return self.PCF8591.read(self,ychn)

theJoystick=Joystick(0x48,0x0,0x1)
while True:
  print(theJoystick.getX(theJoystick.xchn) +",\t" + theJoystick.getY(theJoystick.ychn))
  time.sleep(0.1)