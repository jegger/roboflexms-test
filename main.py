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
#client = ModbusClient('192.168.0.10', port=502)
client = ModbusClient('192.168.50.238', port=502)
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

#UI
def ui():
    var = raw_input("Exit yet?: (y/n)")
    print "you entered ", var
    if var=="y":
        return
    
    var = raw_input("reset safety?: (y/n)")
    print "you entered ", var
    if var=="y":
        reset_safety()
        return
    
    var = raw_input("Send cubes?: (y/n)")
    print "you entered ", var
    if var=="y":
        send_cubes()
        return
#UI END

def reset_safety():
    rq = client.write_coil(8480, True)
    time.sleep(1.5)
    rq = client.write_coil(8480, False)
    print "done"
    

def send_cubes():
    #wirte array
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


ui()