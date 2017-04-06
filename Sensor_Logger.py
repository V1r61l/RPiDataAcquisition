#!/usr/bin/python
import os
import time
import glob
import Sensors_Repository as rep
from sense_hat import SenseHat

# global variables - intervals between readings
SECONDS_60=60
MINUTES_45=45 * SECONDS_60
MINUTES_60=60 * SECONDS_60

# initialize the sense HAT Add-On
sense = SenseHat()

# created the database and the underlying table
rep.create_table()

# read the temperature, humidty and pressure from the HAT
# prepare table line
# round-up the values and save them 
while True:
    table_row = []

    # read each value
    temperature = sense.get_temperature()
    humidity    = sense.get_humidity()
    pressure    = sense.get_pressure()

    # construct the sensor list
    table_row.append(round(temperature,2))
    table_row.append(round(humidity,2))
    table_row.append(round(pressure,2))

    # store values in database
    rep.data_insert(table_row[0], table_row[1], table_row[2])

    # print the values in the terminal
    print("--------------------------------------")
    print("Temperature value is = %s C" % temperature)
    print("Humidity value is = %s %%rH" % humidity)
    print("Pressure value is = %s Millibars" % pressure)
    print("--------------------------------------")
    
    # interval - wait for
    time.sleep(SECONDS_60)

    # print on the HAT display
    sense.show_message("Temp %s"  % table_row[0])
    sense.show_message("Hum %s"   % table_row[1])
    sense.show_message("Press %s" % table_row[2])


    
