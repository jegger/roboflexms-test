#!/usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time
import depot

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

lis=[{'x':1, 'y':2, 'z':3, 'rot':5, 'type':4},
     {'x':6, 'y':7, 'z':8, 'rot':10, 'type':9},
     {'x':11, 'y':12, 'z':13, 'rot':15, 'type':14},
     {'x':16, 'y':17, 'z':18, 'rot':20, 'type':19},
     {'x':21, 'y':22, 'z':23, 'rot':25, 'type':24},
     {'x':26, 'y':27, 'z':28, 'rot':30, 'type':29}]

lis=depot.depot

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
    #write rot
    rq = client.write_register(c, cube['typ'])
    c+=1
    #write type
    rq = client.write_register(c, cube['rot'])
    c+=1

#close connection
client.close()
