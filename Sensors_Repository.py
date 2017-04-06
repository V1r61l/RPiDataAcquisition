import os
import sqlite3
from SensorNo    import s_01
from SensorTypes import ENVIRONMENT_01


db_filename = '/home/pi/Documents/Personal Projects/Cloud Sensors Data Logger/SQLITE_DB/Sensors.db'
db_is_new = not os.path.exists(db_filename)

def create_table():
    try:
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        create_stmt = 'CREATE TABLE IF NOT EXISTS SensorReadings( Id            INTEGER PRIMARY KEY AUTOINCREMENT \
                                                                                NOT NULL   \
                                                                                UNIQUE,    \
                                                                  Sensor_No     INTEGER,   \
                                                                  Sensor_Type   CHAR(30),  \
                                                                  Temperature   DOUBLE,    \
                                                                  Humidity      DOUBLE,    \
                                                                  Pressure      DOUBLE,     \
                                                                  GPS           CHAR,       \
                                                                  Datestamp     DATETIME )'
        c.execute(create_stmt)
        if db_is_new:
            print('Schema does not exist. Creating it ... ')
        else:
            print('Database already exists. It is assumed that schema also exists. ')
        conn.commit()
    except Exception as ex:
        conn.rollback()
        raise ex
    finally:
        c.close()
        conn.close()

def data_insert(temp, hum, lum):
    try:
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        insert_stmt = "INSERT INTO SensorReadings (Sensor_No, Sensor_Type, Temperature, Humidity, Pressure, Datestamp) \
                                           VALUES ((?), (?), (?), (?), (?), DATETIME('now','localtime'))"
        c.execute(insert_stmt, [s_01, ENVIRONMENT_01, temp, hum, lum])
        conn.commit()
    except Exception as ex:
        conn.rollback()
        raise ex
    finally:
        c.close()
        conn.close()

# refactoring idea make the SELECT statements global constants
# make a generic retrieve method
##
##def get_all():
##    conn = sqlite3.connect(db_filename)
##    c = conn.cursor()
##    select_stmt = 'SELECT * FROM Sensors'
##    c.execute(select_stmt)
##    all_rows = c.fetchall()
##    c.close()
##    conn.close()
##    return all_rows
##
##def get_all_temperature_values():
##    conn = sqlite3.connect(db_filename)
##    c = conn.cursor()
##    select_temp_values = 'SELECT datestamp,temperature FROM Sensors'
##    c.execute(select_temp_values)
##    temp_values = c.fetchall()
##    c.close()
##    conn.close()
##    return temp_values
##
##def get_all_humidity_values():
##    conn = sqlite3.connect(db_filename)
##    c = conn.cursor()
##    select_hum_values = 'SELECT datestamp,humidity FROM Sensors'
##    c.execute(select_hum_values)
##    hum_values = c.fetchall()
##    c.close()
##    conn.close()
##    return hum_values
##
##def get_all_luminosity_values():
##    conn = sqlite3.connect(db_filename)
##    c = conn.cursor()
##    select_lum_values = 'SELECT datestamp,luminosity FROM Sensors'
##    c.execute(select_lum_values)
##    lum_values = c.fetchall()
##    c.close()
##    conn.close()
##    return lum_values
##
##def get_maximum_luminosity_value():
##    conn = sqlite3.connect(db_filename)
##    c = conn.cursor()
##    select_max_val_stmt = 'SELECT MAX(luminosity) FROM Sensors'
##    c.execute(select_max_val_stmt)
##    hum_max_value = c.fetchone()
##    c.close()
##    conn.close()
##    return hum_max_value





