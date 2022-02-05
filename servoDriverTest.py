import serial, time
ser = serial.Serial('/dev/ttyUSB' + input("Input USB number: "), baudrate=9600) # open serial port
time.sleep(3)
ser.write(b's0\na\n')
while True:
    ser.write(b'w0\n')
    time.sleep(2)
    ser.write(b'w90\n')
    time.sleep(2)