import serial  #khai bathu vien 
from time import sleep

ser = serial.Serial('/dev/ttyACM0',9600) #mo cong serial voi baudrate 9600

try:
			while(True):
					if (ser.in_waiting >0):  #neu cos tin hieu tu arduino
						data=ser.readline() #doc vao data
						print(data)
					else:
						string = input('what do you send?')
						#string = string + "\r"
						ser.write(string.encode()) #chuyen ve unicode va dua ra cho arrduino
						sleep(0.5)
except KeyboardInterrupt:
	print('done')
finally:
	ser.close() #dong cong serial
