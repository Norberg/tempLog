import serial, re

def getTemp():
	ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=10)
	ser.open()
	value = ser.readline()
	ser.close()
	#conversation done acording to maxim-ic documentation for DS18S20
	try:
		rom = re.split(" P=|R=|CRC=", value)[1]
		prog = re.split(" P=|R=|CRC=", value)[2]
		TEMP_LSB = int(prog.split(' ')[1], 16)
		TEMP_MSB = int(prog.split(' ')[2], 16)
		COUNT_REMAIN = int(prog.split(' ')[7], 16)
	except:
		if re.match("No more addresses.", value) is not None:
			return 0.0, "null"	
		return getTemp()

	if (TEMP_MSB == 0):
		#positve temerature
		TEMP_READ = TEMP_LSB*0.5 
	else:
		#negative temperature
		TEMP_READ = (TEMP_LSB-256)*0.5 
	#get extended temperature
	TEMPERATURE = TEMP_READ - 0.25 * ((16.0 - COUNT_REMAIN)/ 16.0)
	return round(TEMPERATURE, 1), rom

def main():
	temp, rom = getTemp()
	print "ROM:", rom, "Temp: ", temp, "C"

if __name__ == "__main__":
	main()
