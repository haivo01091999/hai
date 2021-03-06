import serial                   #Khai bao thu vien Serial
from time import sleep          #Khai bao lenh sleep tu thu vien time

ser = serial.Serial('/dev/ttyACM0',9600)                #Mo cong Serial baudrat

try:
        while (True):
                if (ser.in_waiting>0):                  #Neu co tin hieu tu Arduino
                        data = ser.readline()           #Doc vao data
                        print(data)                     #In ra man hinh
                else:                                   #Nguoc lai
                        string=input('What do you want to send? ')  #neu la python 3 thi dung input, python 2.X thi dung raw_input
                        string=string+"\r"                          #Cong them ki tu \r
                        ser.write(string.encode())                  #Encode va xuat ra arduino
                        sleep(0.5)                                  #Dung 0.5s
except KeyboardInterrupt:                                           #Nhan Ctrl+C
        print('Done')                                               #In ra Done
finally:
        ser.close()                                     #Cuoi cung dong cong Serial
