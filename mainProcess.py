# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from daemon import daemon
import subprocess, time, sys, sqlite3, time, logging

def bash_command(cmd):
	subprocess.Popen(cmd, shell=True)

conn = sqlite3.connect('plantino_record.db')

class MyDaemon(daemon):
	def run(self):
		while True:

			query = conn.execute("SELECT * FROM selectedPlant")

			selectedPlant = query.fetchone()
			minTemp = int(selectedPlant[2])
			maxTemp = int(selectedPlant[3])
			minHum = int(selectedPlant[4])
			maxHum = int(selectedPlant[5])
			minLight = int(selectedPlant[6])
			maxLight = int(selectedPlant[7])

			if selectedPlant !=  None:

				for x in xrange(1,10):

					temperature = bash_command("cat" "/sys/devices/virtual/input/input1/temperature")
					moist = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A5_raw")
					light = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A0_raw")

					if int(temperature) <= minTemp:
						bash_command()
					else:
						bash_command()
								
					if int(moist) <= minHum:
						bash_command()
					else:
						bash_command()
								
					if int(light) <= minLight:
						bash_command()
					else:
						bash_command()			

					time.sleep(35)

				mTemperature = bash_command("cat" "/sys/devices/virtual/input/input1/temperature")
				mMoist = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A5_raw")
				mLight = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A0_raw")

				conn.execute("INSERT INTO temperatures (temp) VALUES (?)"(mTemperature,))
				conn.execute("INSERT INTO humidity (moist) VALUES (?)"(mMoist,))
				conn.execute("INSERT INTO sunLight (light) VALUES (?)"(mLight,))

				conn.close()
					
if __name__ == "__main__":
	daemon = MyDaemon('/tmp/plantino.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)