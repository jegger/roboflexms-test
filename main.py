#!/usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

#create logger
"""import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)"""

#create connection
client = ModbusClient('192.168.0.10', port=502)
client.connect()

"""
#do testes
rq = client.write_register(0, 255)
rq = client.write_register(1, 50)
rq = client.write_register(2, 20)
rq = client.write_register(3, 30)
rq = client.write_register(4, 40)
rq = client.write_register(5, 50)
rq = client.write_register(6, 60)
rq = client.write_register(7, 70)    
rq = client.write_register(8, 80)
rq = client.write_register(9, 90)
rq = client.write_register(530, 154)
rq = client.write_coil(8480, False)
"""

lis=[{'x':0, 'y':2, 'z':0, 'rot':0, 'type':0},
     {'x':0, 'y':6, 'z':1, 'rot':0, 'type':0},
     {'x':21, 'y':0, 'z':2, 'rot':0, 'type':0},
     {'x':0, 'y':0, 'z':3, 'rot':0, 'type':0},
     {'x':0, 'y':0, 'z':4, 'rot':0, 'type':0},
     {'x':0, 'y':0, 'z':5, 'rot':0, 'type':0}]

#clear all registers
for reg in range(530):
    rq = client.write_register(reg, 0)

#set coil 'new anlage arrived to false'
rq = client.write_coil(8480, False)

#write cubes into PLC
c=0
for cube in lis:
    #write x
    rq = client.write_register(c, cube['x'])
    c+=1
    #write y
    rq = client.write_register(c, cube['y'])
    c+=1
    #write z
    rq = client.write_register(c, cube['z'])
    c+=1
    print cube['z'], c
    #write rot
    rq = client.write_register(c, cube['rot'])
    c+=1
    #write type
    rq = client.write_register(c, cube['type'])
    c+=1

#close connection
client.close()
