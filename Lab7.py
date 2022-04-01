from pyqtgraph.Qt import QtGui, QtCore 
import pyfirmata2
import pyqtgraph as pg 
 
from pyfirmata2 import Arduino, util 
import time 
 
port= pyfirmata2.Arduino.AUTODETECT
board=pyfirmata2.Arduino(port)

it=util.Iterator(board) 
it.start() 
 
app=QtGui.QApplication([]) 
win=pg.GraphicsWindow(title='Tiempo Real') 
p=win.addPlot(title='Grafica en tiempo real') 
curva=p.plot(pen='y') 
 
p.setRange(yRange=[-10,100]) 
dataX=[] 
dataY=[] 
lastY=0 
 
analog0=board.get_pin('a:0:i') 
 
def Update(): 
    global curva, dataX, dataY, lastY, nuevoDato 

    dato=analog0.read() 
    if dato is not None: 
       nuevoDato=dato*100 
       print (nuevoDato) 
       time.sleep(1) 
    else: 
        nuevoDato=0 

    dataX.append (nuevoDato) 
    dataY.append (lastY) 
    lastY+=1 

    if len(dataX)>200: 
        dataX=dataX[:-1] 
        dataY=dataY[:-1] 

    curva.setData(dataY, dataX) 
    QtGui.QApplication.processEvents() 


try: 
    while True: Update() 

except KeyboardInterrupt: 
    pg. QtGui. Application.exec() 
    board.exit()