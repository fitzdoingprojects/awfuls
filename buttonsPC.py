import sys
import serial
buttons = ['0', '0', '0', '0', '0', '0', '0', '0', ]
ser = serial.Serial('COM4') #on pc (windows)
def getButtons():
        data = ser.readline()
        buttons[0] = data[0:1]
        buttons[1] = data[1:2]
        buttons[2] = data[2:3]
        buttons[3] = data[3:4]
        print(buttons)