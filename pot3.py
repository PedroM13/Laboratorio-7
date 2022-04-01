import pyfirmata2

from pyfirmata2 import Arduino, util 
import time 
 
port= pyfirmata2.Arduino.AUTODETECT
board=pyfirmata2.Arduino(port)

it=util.Iterator(board) 
it.start() 
 
 
analog0=board.get_pin('a:0:i') 

while True:
    dato=analog0.read() 
    if dato is not None and dato > 0.95:
      board.digital[3].write(1)
      time.sleep(.5)
      board.digital[3].write(0) 
      time.sleep(.1)