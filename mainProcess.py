#!/usr/bin/env python

import subprocess, time, sys, sqlite3, json
from daemon import Daemon

def bash_command(cmd):
	subprocess.Popen(cmd, shell=True)

plantName = "basil"
conn = sqlite3.connect('plantino_record') #path da cambiare, mettere nella sd

with open ('data.json') as plants_file:
	data = json.load(plants_file)
 
class MyDaemon(Daemon):
        def run(self):
                while True:
						if plantName ==  data["plants"][0]["name"]
							
							for x in xrange(1,10):

								basilTemperature = bash_command("cat" "/sys/devices/virtual/input/input1/temperature")
								basilMoist = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A5_raw")
								basilLight = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A0_raw")

								if (int)basilTemperature <= data["plants"][0][minTemperature]:
									bash_command()
								else
									bash_command()

								time.sleep(5)

						if plantName ==  data["plants"][1]["name"]
							
							for x in xrange(1,10):

								oreganoTemperature = bash_command("cat" "/sys/devices/virtual/input/input1/temperature")
								oreganoMoist = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A5_raw")
								oreganoLight = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A0_raw")

								if (int)oreganoTemperature <= data["plants"][1][minTemperature]:
									bash_command()
								else
									bash_command()

								time.sleep(5)

						if plantName ==  data["plants"][2]["name"]
							
							for x in xrange(1,10):

								sageTemperature = bash_command("cat" "/sys/devices/virtual/input/input1/temperature")
								sageMoist = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A5_raw")
								sageLight = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A0_raw")

								if (int)sageTemperature <= data["plants"][2][minTemperature]:
									bash_command()
								else
									bash_command()

								time.sleep(5)

						if plantName ==  data["plants"][3]["name"]
							
							for x in xrange(1,10):

								spinachTemperature = bash_command("cat" "/sys/devices/virtual/input/input1/temperature")
								spinachMoist = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A5_raw")
								spinachLight = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A0_raw")

								if (int)spinachTemperature <= data["plants"][3][minTemperature]:
									bash_command()
								else
									bash_command()

								time.sleep(5)

						mTemperature = bash_command("cat" "/sys/devices/virtual/input/input1/temperature")
						mMoist = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A5_raw")
						mLight = bash_command("cat" "/sys/bus/iio/devices/iio:device0/in_voltage_A0_raw")

						conn.execute("INSERT INTO temperatures (temp) VALUES (?)"(mTemperature,))
						conn.execute("INSERT INTO humidity (moist) VALUES (?)"(mMoist,))
						conn.execute("INSERT INTO sunLight (light) VALUES (?)"(mLight,))

						conn.close()

 
if __name__ == "__main__":
        daemon = MyDaemon('/tmp/plantino_record.pid')
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