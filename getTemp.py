import serial

def getTemp():
	ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=10)
	ser.open()
	ser.flushInput()
	value = ser.read(51)
	ser.flush()
	ser.close()
	#conversation done acording to maxim-ic documentation for DS18S20
	try:
		TEMP_LSB = int(value.split(' ')[9], 16)
		TEMP_MSB = int(value.split(' ')[10], 16)
		COUNT_REMAIN = int(value.split(' ')[15], 16)
	except:
		print "DEBUG", value
		quit()
	if (TEMP_MSB == 0):
		#positve temerature
		TEMP_READ = TEMP_LSB*0.5 
	else:
		#negative temperature
		TEMP_READ = (TEMP_LSB-256)*0.5 
	#get extended temperature
	TEMPERATURE = TEMP_READ - 0.25 * ((16.0 - COUNT_REMAIN)/ 16.0)
	return round(TEMPERATURE, 1)

def main():
	print getTemp(), "C"

if __name__ == "__main__":
	main()
